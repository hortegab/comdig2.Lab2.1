#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Cosenoalzado
# Generated: Sat Feb 23 18:51:05 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import numpy
import sip
import sys
import wform  # embedded python module
from gnuradio import qtgui


class cosenoalzado(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Cosenoalzado")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Cosenoalzado")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "cosenoalzado")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.Sps = Sps = 8
        self.Rb = Rb = 32000
        self.samp_rate = samp_rate = Rb*Sps
        self.run_stop = run_stop = True
        self.rolloff = rolloff = 0.5
        self.ntaps = ntaps = Sps*16
        self.Delay_rect = Delay_rect = 0
        self.Delay_all = Delay_all = 0
        self.Delay_RRC = Delay_RRC = 0
        self.Delay_RC = Delay_RC = 0
        self.Delay_Nyquist = Delay_Nyquist = 0

        ##################################################
        # Blocks
        ##################################################
        self._ntaps_range = Range(Sps, Sps*1024, Sps, Sps*16, 200)
        self._ntaps_win = RangeWidget(self._ntaps_range, self.set_ntaps, 'ntaps', "counter_slider", int)
        self.top_grid_layout.addWidget(self._ntaps_win, 0, 2, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._rolloff_range = Range(0.1, 1.0, 0.1, 0.5, 200)
        self._rolloff_win = RangeWidget(self._rolloff_range, self.set_rolloff, 'Roll off', "counter_slider", float)
        self.top_grid_layout.addWidget(self._rolloff_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.pestana = Qt.QTabWidget()
        self.pestana_widget_0 = Qt.QWidget()
        self.pestana_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_0)
        self.pestana_grid_layout_0 = Qt.QGridLayout()
        self.pestana_layout_0.addLayout(self.pestana_grid_layout_0)
        self.pestana.addTab(self.pestana_widget_0, 'Datos')
        self.pestana_widget_1 = Qt.QWidget()
        self.pestana_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_1)
        self.pestana_grid_layout_1 = Qt.QGridLayout()
        self.pestana_layout_1.addLayout(self.pestana_grid_layout_1)
        self.pestana.addTab(self.pestana_widget_1, 'Espectro')
        self.pestana_widget_2 = Qt.QWidget()
        self.pestana_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_2)
        self.pestana_grid_layout_2 = Qt.QGridLayout()
        self.pestana_layout_2.addLayout(self.pestana_grid_layout_2)
        self.pestana.addTab(self.pestana_widget_2, 'Diagrama de Ojo')
        self.top_grid_layout.addWidget(self.pestana)
        self._Delay_rect_range = Range(0, ntaps*2, 1, 0, 200)
        self._Delay_rect_win = RangeWidget(self._Delay_rect_range, self.set_Delay_rect, 'Retraso Rect', "counter_slider", int)
        self.top_grid_layout.addWidget(self._Delay_rect_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._Delay_all_range = Range(0, ntaps*10000, Sps, 0, 200)
        self._Delay_all_win = RangeWidget(self._Delay_all_range, self.set_Delay_all, 'Retraso todo', "counter_slider", int)
        self.top_grid_layout.addWidget(self._Delay_all_win, 1, 4, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._Delay_RRC_range = Range(0, ntaps*10000, Sps, 0, 200)
        self._Delay_RRC_win = RangeWidget(self._Delay_RRC_range, self.set_Delay_RRC, 'Retraso RRC', "counter_slider", int)
        self.top_grid_layout.addWidget(self._Delay_RRC_win, 1, 3, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._Delay_RC_range = Range(0, ntaps*10000, Sps, 0, 200)
        self._Delay_RC_win = RangeWidget(self._Delay_RC_range, self.set_Delay_RC, 'Retraso RC', "counter_slider", int)
        self.top_grid_layout.addWidget(self._Delay_RC_win, 1, 2, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._Delay_Nyquist_range = Range(0, ntaps*10000, Sps, 0, 200)
        self._Delay_Nyquist_win = RangeWidget(self._Delay_Nyquist_range, self.set_Delay_Nyquist, 'Retraso Nyq', "counter_slider", int)
        self.top_grid_layout.addWidget(self._Delay_Nyquist_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        _run_stop_check_box = Qt.QCheckBox('Inicial/Parar')
        self._run_stop_choices = {True: True, False: False}
        self._run_stop_choices_inv = dict((v,k) for k,v in self._run_stop_choices.iteritems())
        self._run_stop_callback = lambda i: Qt.QMetaObject.invokeMethod(_run_stop_check_box, "setChecked", Qt.Q_ARG("bool", self._run_stop_choices_inv[i]))
        self._run_stop_callback(self.run_stop)
        _run_stop_check_box.stateChanged.connect(lambda i: self.set_run_stop(self._run_stop_choices[bool(i)]))
        self.top_grid_layout.addWidget(_run_stop_check_box, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0_0_0_0 = qtgui.time_sink_f(
        	ntaps, #size
        	samp_rate, #samp_rate
        	"Wave Forming", #name
        	4 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_0_0.set_y_axis(-1.2, 1.2)

        self.qtgui_time_sink_x_0_0_0_0_0.set_y_label('RC Filter Poly', "")

        self.qtgui_time_sink_x_0_0_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0_0_0_0.disable_legend()

        labels = [' Nyq', 'RC', 'RRC', 'Rect', '',
                  '', '', '', '', '']
        widths = [3, 3, 3, 3, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [0, 0, 0, 0, 1,
                  1, 1, 1, 1, 1]
        markers = [0, 0, 0, 0, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(4):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.pestana_grid_layout_0.addWidget(self._qtgui_time_sink_x_0_0_0_0_0_win)
        self.blocks_vector_source_x_0_3_0 = blocks.vector_source_f((ntaps-Sps-int(ntaps/2)+1)*[0.,]+Sps*[1.,]+int(ntaps/2-1)*[0.,], True, 1, [])
        self.blocks_vector_source_x_0_2 = blocks.vector_source_f(wform.rrcos(Sps,ntaps,rolloff), True, 1, [])
        self.blocks_vector_source_x_0_1 = blocks.vector_source_f(wform.rcos(Sps,ntaps,rolloff), True, 1, [])
        self.blocks_vector_source_x_0_0 = blocks.vector_source_f(wform.nyq(Sps,ntaps), True, 1, [])
        self.blocks_throttle_0_0_0_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_delay_0_0_1 = blocks.delay(gr.sizeof_float*1, Delay_RRC+Delay_all)
        self.blocks_delay_0_0_0 = blocks.delay(gr.sizeof_float*1, Delay_Nyquist+Delay_all)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_float*1, Delay_RC+Delay_all)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, Delay_rect+Delay_all)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_delay_0, 0), (self.blocks_throttle_0_0_0_0, 0))
        self.connect((self.blocks_delay_0_0, 0), (self.qtgui_time_sink_x_0_0_0_0_0, 1))
        self.connect((self.blocks_delay_0_0_0, 0), (self.qtgui_time_sink_x_0_0_0_0_0, 0))
        self.connect((self.blocks_delay_0_0_1, 0), (self.qtgui_time_sink_x_0_0_0_0_0, 2))
        self.connect((self.blocks_throttle_0_0_0_0, 0), (self.qtgui_time_sink_x_0_0_0_0_0, 3))
        self.connect((self.blocks_vector_source_x_0_0, 0), (self.blocks_delay_0_0_0, 0))
        self.connect((self.blocks_vector_source_x_0_1, 0), (self.blocks_delay_0_0, 0))
        self.connect((self.blocks_vector_source_x_0_2, 0), (self.blocks_delay_0_0_1, 0))
        self.connect((self.blocks_vector_source_x_0_3_0, 0), (self.blocks_delay_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "cosenoalzado")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.set_ntaps(self.Sps*16)
        self.set_samp_rate(self.Rb*self.Sps)
        self.blocks_vector_source_x_0_3_0.set_data((self.ntaps-self.Sps-int(self.ntaps/2)+1)*[0.,]+self.Sps*[1.,]+int(self.ntaps/2-1)*[0.,], [])
        self.blocks_vector_source_x_0_2.set_data(wform.rrcos(self.Sps,self.ntaps,self.rolloff), [])
        self.blocks_vector_source_x_0_1.set_data(wform.rcos(self.Sps,self.ntaps,self.rolloff), [])
        self.blocks_vector_source_x_0_0.set_data(wform.nyq(self.Sps,self.ntaps), [])

    def get_Rb(self):
        return self.Rb

    def set_Rb(self, Rb):
        self.Rb = Rb
        self.set_samp_rate(self.Rb*self.Sps)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0_0_0_0_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0_0_0_0.set_sample_rate(self.samp_rate)

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        self._run_stop_callback(self.run_stop)
        if self.run_stop: self.start()
        else: self.stop(); self.wait()

    def get_rolloff(self):
        return self.rolloff

    def set_rolloff(self, rolloff):
        self.rolloff = rolloff
        self.blocks_vector_source_x_0_2.set_data(wform.rrcos(self.Sps,self.ntaps,self.rolloff), [])
        self.blocks_vector_source_x_0_1.set_data(wform.rcos(self.Sps,self.ntaps,self.rolloff), [])

    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps
        self.blocks_vector_source_x_0_3_0.set_data((self.ntaps-self.Sps-int(self.ntaps/2)+1)*[0.,]+self.Sps*[1.,]+int(self.ntaps/2-1)*[0.,], [])
        self.blocks_vector_source_x_0_2.set_data(wform.rrcos(self.Sps,self.ntaps,self.rolloff), [])
        self.blocks_vector_source_x_0_1.set_data(wform.rcos(self.Sps,self.ntaps,self.rolloff), [])
        self.blocks_vector_source_x_0_0.set_data(wform.nyq(self.Sps,self.ntaps), [])

    def get_Delay_rect(self):
        return self.Delay_rect

    def set_Delay_rect(self, Delay_rect):
        self.Delay_rect = Delay_rect
        self.blocks_delay_0.set_dly(self.Delay_rect+self.Delay_all)

    def get_Delay_all(self):
        return self.Delay_all

    def set_Delay_all(self, Delay_all):
        self.Delay_all = Delay_all
        self.blocks_delay_0_0_1.set_dly(self.Delay_RRC+self.Delay_all)
        self.blocks_delay_0_0_0.set_dly(self.Delay_Nyquist+self.Delay_all)
        self.blocks_delay_0_0.set_dly(self.Delay_RC+self.Delay_all)
        self.blocks_delay_0.set_dly(self.Delay_rect+self.Delay_all)

    def get_Delay_RRC(self):
        return self.Delay_RRC

    def set_Delay_RRC(self, Delay_RRC):
        self.Delay_RRC = Delay_RRC
        self.blocks_delay_0_0_1.set_dly(self.Delay_RRC+self.Delay_all)

    def get_Delay_RC(self):
        return self.Delay_RC

    def set_Delay_RC(self, Delay_RC):
        self.Delay_RC = Delay_RC
        self.blocks_delay_0_0.set_dly(self.Delay_RC+self.Delay_all)

    def get_Delay_Nyquist(self):
        return self.Delay_Nyquist

    def set_Delay_Nyquist(self, Delay_Nyquist):
        self.Delay_Nyquist = Delay_Nyquist
        self.blocks_delay_0_0_0.set_dly(self.Delay_Nyquist+self.Delay_all)


def main(top_block_cls=cosenoalzado, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
