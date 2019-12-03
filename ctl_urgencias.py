import gi
import time
import sys
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from mod_urgencias import *
from ei.arboles import AHeap
from ei.recorridos import pre_orden


class Urgencias_ctl:
    def __init__(self):
        # sys.setrecursionlimit(10000)
        self.arb_heap = AHeap()
        gui = Gtk.Builder()
        gui.add_from_file("gui_urgencias.glade")

        # Lista de enventos de las acciones de la interfaz
        eventos = {'on_window_delete_event': Gtk.main_quit,
                   'on_img_about_activate': self.on_img_about_activate,
                   'on_about_delete_event': self.on_about_delete_event,
                   'on_cbx_id_changed': self.on_cbx_id_changed,
                   'on_btn_añadir_clicked': self.on_btn_añadir_clicked,
                   'on_btn_siguiente_clicked': self.on_btn_siguiente_clicked,
                   'on_btn_cancelar_clicked': self.on_btn_cancelar_clicked,
                   'on_btn_atendido_clicked': self.on_btn_atendido_clicked
                   }
        # Conexion de los eventos al enlace de la interfaz
        gui.connect_signals(eventos)
        self.mi_admin = Administracion()
        self.ventana = gui.get_object('window')
        self.ventana.set_title('Sistema de Atención de Urgencias')
        self.about = gui.get_object('about')

        self.listS_triaje = Gtk.ListStore(str, int, bool)
        self.listS_historial = Gtk.ListStore(str, str)
        self.listS_id = Gtk.ListStore(str)
        self.listS_eps = Gtk.ListStore(str)
        self.listS_eps.append(['COOMEVA'])
        self.listS_eps.append(['COMFAMILIAR'])
        self.listS_eps.append(['EMSSANAR'])
        self.listS_eps.append(['NUEVA EPS'])
        self.listS_eps.append(['SANITAS'])

        ''' Seccion de Urgencias '''
        self.cbx_id = gui.get_object('cbx_id')
        self.cbx_id.set_model(self.listS_id)
        self.cbx_id.set_entry_text_column(0)

        self.entC_id = gui.get_object('entC_id')
        self.entC_id.set_model(self.listS_id)
        self.mi_admin.init_list_id(self.listS_id)
        self.entC_id.set_text_column(0)

        self.ent_nombre_urg = gui.get_object('ent_nombre_urg')
        self.ent_telefono_urg = gui.get_object('ent_telefono_urg')
        self.spnB_edad = gui.get_object('spnB_edad')
        self.cbxT_eps = gui.get_object('cbxT_eps')
        self.cbxT_eps.set_model(self.listS_eps)
        self.ent_obs_urg = gui.get_object('ent_obs_urg')
        self.trv_triajes = gui.get_object('trv_triajes')
        self.btn_añadir = gui.get_object('btn_añadir')

        ''' Seccion de Atencion '''
        self.btn_siguiente = gui.get_object('btn_siguiente')
        self.ent_id_ate = gui.get_object('ent_id_ate')
        self.ent_nombre_ate = gui.get_object('ent_nombre_ate')
        self.ent_edad_asi = gui.get_object('ent_edad_asi')
        self.ent_telefono_ate = gui.get_object('ent_telefono_ate')
        self.ent_eps_ate = gui.get_object('ent_eps_ate')
        self.ent_triaje_ate = gui.get_object('ent_triaje_ate')
        self.ent_pri_ate = gui.get_object('ent_pri_ate')
        self.ent_obs_ate = gui.get_object('ent_obs_ate')
        self.trv_historial = gui.get_object('trv_historial')
        self.btn_cancelar = gui.get_object('btn_cancelar')
        self.btn_atendido = gui.get_object('btn_atendido')

        # Definir los TreeView
        self.__definir_treeViews()
        # Cargar urgencias pendientes de ser atendidas al arbol
        self.mi_admin.init_arb_heap_inicial(self.arb_heap)
        # pre_orden(self.arb_heap)

        self.ventana.show()

    def on_img_about_activate(self, widget):
        pre_orden(self.arb_heap)
        self.about.run()

    def on_cbx_id_changed(self, widget):
        pac_dummy = Paciente(id='')
        self.__reiniciar_campos_urgencias(pac_dummy)
        id = widget.get_child().get_text()
        if id:
            paciente = self.mi_admin.get_paciente(id)
            if paciente is not None:
                self.__desactivar_entradas_urgencias()
                self.__reiniciar_campos_urgencias(paciente)
                widget.disconnect_by_func(self.on_cbx_id_changed)
                for i in range(len(self.listS_id)):
                    path = Gtk.TreePath(i)
                    if self.listS_id[path] == id:
                        widget.set_active(path)
                widget.connect('changed', self.on_cbx_id_changed)
            else:
                self.__activar_entradas_urgencias()

    def on_btn_añadir_clicked(self, widget):
        try:
            id = self.cbx_id.get_child().get_text()
            nom = self.ent_nombre_urg.get_text().upper()
            tel = self.ent_telefono_urg.get_text()
            edad = self.spnB_edad.get_value_as_int()
            item = self.cbxT_eps.get_active()
            if item != -1:
                eps = self.listS_eps[item][0]
            if id != '' and nom != '' and item != -1:
                pac = self.mi_admin.get_paciente(id)
                if pac is None:
                    pac = Paciente(int(id), nom, tel, edad, eps)
                    self.mi_admin.agregar_paciente(pac)
                    self.mi_admin.init_list_id(self.listS_id)
                triaje = None
                for tri in self.listS_triaje:
                    if tri[2]:
                        triaje = self.mi_admin.get_triaje(tri[1])
                if triaje is not None:
                    fecha = time.strftime('%d/%m/%y')+' '+time.strftime('%H:%M:%S')
                    cod_urg = self.mi_admin.get_conse_cod_urg()
                    obs = self.ent_obs_urg.get_text()
                    urg = Urgencia(cod_urg, pac, triaje, obs, fecha, False)
                    self.arb_heap.agregar(urg)
                    self.mi_admin.agregar_urgencia(urg)
                    self.__reiniciar_campos_urgencias(Paciente(id=''))
                    self.cbx_id.get_child().set_text('')
                else:
                    self.__mensaje(None, 'Debe seleccionar el triaje de la emergencia.')
            else:
                self.__mensaje(None, 'Debe diligenciar todos los campos.')
        except ValueError:
            self.__mensaje(None, 'Numero de identificación no permite caracteres.')

    def on_btn_siguiente_clicked(self, widget):
        urg_cima = self.arb_heap.traer_cima()
        if urg_cima is not None:
            pac = self.mi_admin.get_paciente(urg_cima.get_paciente().get_id())
            tri = self.mi_admin.get_triaje(urg_cima.get_triaje().get_codigo())
            obs = urg_cima.get_observacion()
            self.__reiniciar_campos_atencion(pac, tri, obs)
            self.mi_admin.init_listS_historial(self.listS_historial, pac.get_id())
        else:
            self.__mensaje(None, 'No hay urgencias por el momento.')
    def on_btn_cancelar_clicked(self, widget):
        mensaje = ('Esta a punto de ignorar una urgencia. \n' +
                   '¿Desea realizar la cancelación?')
        if self.__mensaje_confirmacion(None, mensaje):
            self.arb_heap.remover_cima()
            self.__reiniciar_campos_atencion(Paciente(id=''), Triaje(cod_tri=''))

    def on_btn_atendido_clicked(self, widget):
        id_pac = self.ent_id_ate.get_text()
        if id_pac != '':
            urg = self.arb_heap.traer_cima()
            self.mi_admin.update_estado_urgencia(urg.get_codigo())
            self.arb_heap.remover_cima()
            pac = Paciente(id='')
            tri = Triaje(cod_tri='')
            self.__reiniciar_campos_atencion(pac, tri)
        else:
            self.__mensaje(None, 'No hay paciente seleccionado.')

    def on_about_delete_event(self, widget, otro):
        self.about.hide()

    def __definir_treeViews(self):
        ''' TreeView Triajes '''
        self.trv_triajes.set_model(self.listS_triaje)
        # Primera columna: descripcion
        renderer_des = Gtk.CellRendererText()
        column_des = Gtk.TreeViewColumn('Descripción', renderer_des, text=0)
        self.trv_triajes.append_column(column_des)
        # Segunda columna: prioridad
        renderer_pri = Gtk.CellRendererText()
        column_pri = Gtk.TreeViewColumn('Prioridad', renderer_pri, text=1)
        self.trv_triajes.append_column(column_pri)
        # Tercer columna: RadioButton
        renderer_sel = Gtk.CellRendererToggle()
        renderer_sel.set_radio(True)
        renderer_sel.connect('toggled', self.__on_listS_toggled_active)
        column_sel = Gtk.TreeViewColumn('Selección', renderer_sel, active=2)
        self.trv_triajes.append_column(column_sel)
        # Llenar el ListStore con las triadas
        self.mi_admin.init_listS_triajes(self.listS_triaje)

        ''' TreeView Historial '''
        self.trv_historial.set_model(self.listS_historial)
        # Primera Columna: descripcion
        renderer_fec = Gtk.CellRendererText()
        column_fec = Gtk.TreeViewColumn('Fecha', renderer_fec, text=0)
        self.trv_historial.append_column(column_fec)
        # Segunda columna: fecha
        renderer_his = Gtk.CellRendererText()
        column_his = Gtk.TreeViewColumn('Descripción', renderer_his, text=1)
        self.trv_historial.append_column(column_his)

    def __on_listS_toggled_active(self, widget, path):
        selected_path = Gtk.TreePath(path)
        for row in self.listS_triaje:
            row[2] = (row.path == selected_path)

    def __reiniciar_campos_urgencias(self, un_paciente):
        self.ent_nombre_urg.set_text(un_paciente.get_nombre())
        self.ent_telefono_urg.set_text(un_paciente.get_telefono())
        self.spnB_edad.set_value(un_paciente.get_edad())
        if un_paciente.get_eps() == 'COOMEVA':
            self.cbxT_eps.set_active(0)
        elif un_paciente.get_eps() == 'COMFAMILIAR':
            self.cbxT_eps.set_active(1)
        elif un_paciente.get_eps() == 'EMSSANAR':
            self.cbxT_eps.set_active(2)
        elif un_paciente.get_eps() == 'NUEVA EPS':
            self.cbxT_eps.set_active(3)
        elif un_paciente.get_eps() == 'SANITAS':
            self.cbxT_eps.set_active(3)
        else:
            self.cbxT_eps.set_active(-1)
        for tri in self.listS_triaje:
            tri[2] = False
        self.ent_obs_urg.set_text('')

    def __reiniciar_campos_atencion(self, un_paciente, un_triaje, obs=''):
        self.ent_id_ate.set_text(un_paciente.get_id())
        self.ent_nombre_ate.set_text(un_paciente.get_nombre())
        self.ent_edad_asi.set_text(str(un_paciente.get_edad()))
        self.ent_telefono_ate.set_text(un_paciente.get_telefono())
        self.ent_eps_ate.set_text(un_paciente.get_eps())
        self.ent_triaje_ate.set_text(un_triaje.get_descripcion())
        self.ent_pri_ate.set_text(str(un_triaje.get_prioridad()))
        self.ent_obs_ate.set_text(obs)
        self.listS_historial.clear()

    def __desactivar_entradas_urgencias(self):
        self.cbx_id.set_can_focus(False)
        self.ent_nombre_urg.set_can_focus(False)
        self.ent_telefono_urg.set_can_focus(False)
        self.spnB_edad.set_can_focus(False)
        self.cbxT_eps.set_property("button-sensitivity", Gtk.SensitivityType.OFF)
        # self.ent_obs_urg.set_can_focus(False)

    def __activar_entradas_urgencias(self):
        self.cbx_id.set_can_focus(True)
        self.ent_nombre_urg.set_can_focus(True)
        self.ent_telefono_urg.set_can_focus(True)
        self.spnB_edad.set_can_focus(True)
        self.cbxT_eps.set_property("button-sensitivity", Gtk.SensitivityType.ON)
        # self.ent_obs_urg.set_can_focus(True)

    def __mensaje(self, widget, mensaje):
        flags = Gtk.DialogFlags.DESTROY_WITH_PARENT | Gtk.DialogFlags.MODAL
        dialogo = Gtk.MessageDialog(widget, flags, Gtk.MessageType.INFO,
                                    Gtk.ButtonsType.OK, mensaje)
        dialogo.run()
        dialogo.destroy()

    def __mensaje_confirmacion(self, widget, mensaje):
        flags = Gtk.DialogFlags.DESTROY_WITH_PARENT | Gtk.DialogFlags.MODAL
        dialogo = Gtk.MessageDialog(widget, flags, Gtk.MessageType.INFO,
                                    Gtk.ButtonsType.OK_CANCEL, mensaje)
        respuesta = dialogo.run()
        res = False
        if respuesta == Gtk.ResponseType.OK:
            res = True
        dialogo.destroy()
        return res

if __name__ == '__main__':
    main = Urgencias_ctl()
    Gtk.main()
