class Controller():
    def __init__(self, view, model):
        self.view = view
        self.model = model

    ############################################################
    # Preview
    ############################################################
    def start_video_preview(self):
        print("Start Video Preview")
        self.model.start_video_preview()

    def stop_video_preview(self):
        print("Stop Video Preview")
        self.model.stop_video_preview()

    ############################################################
    # Tracking
    ############################################################
    def start_tracking(self):
        print("Start Video Tracking")
        # TODO: make sure serial model actually created and running
        # TODO: If the serial model already exist, no need to create again.
        self.model.create_serial_model(57600, "COM7")
        self.model.start_tracking()

    def stop_tracking(self):
        print("Stop Video Tracking")
        self.model.stop_tracking()

    ############################################################
    # Recording
    ############################################################
    def start_record(self):
        print("Start Record")
        self.model.start_record()

    def stop_record(self):
        print("Stop Record")
        self.model.stop_record()

    ############################################################
    # Close Event
    ############################################################
    def main_gui_closeEvent(self):
        # Terminate all thread, if any
        self.model.main_gui_closeEvent()

    ############################################################
    # Manual Control
    ############################################################

    ############################################################
    # Manual Control - Gimbal Control
    ############################################################

    def manual_gimbal_up(self):
        self.model.manual_gimbal_up()

    def manual_gimbal_down(self):
        self.model.manual_gimbal_down()

    def manual_gimbal_left(self):
        self.model.manual_gimbal_left()

    def manual_gimbal_right(self):
        self.model.manual_gimbal_right()
