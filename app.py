import cv2
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.clock import Clock


class CameraToggleApp(App):
    def build(self):
        self.camera_index = 0  # Start with the back camera (index 0)
        self.capture = cv2.VideoCapture(self.camera_index)
        
        # Main layout
        self.layout = BoxLayout(orientation="vertical")
        
        # Image widget to display the camera feed
        self.image_widget = Image()
        self.layout.add_widget(self.image_widget)

        # Toggle button
        toggle_button = Button(text="Toggle Camera")
        toggle_button.bind(on_press=self.toggle_camera)
        self.layout.add_widget(toggle_button)
        
        # Schedule the frame update
        Clock.schedule_interval(self.update_frame, 1.0 / 30.0)  # 30 FPS
        
        return self.layout

    def update_frame(self, dt):
        # Read a frame from the camera
        ret, frame = self.capture.read()
        if ret:
            # Convert the frame from BGR to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Get the frame dimensions
            h, w, _ = frame.shape
            
            # Convert the frame to a Kivy texture
            texture = Texture.create(size=(w, h), colorfmt="rgb")
            texture.blit_buffer(frame.tobytes(), colorfmt="rgb", bufferfmt="ubyte")
            texture.flip_vertical()  # Flip the texture to align with the camera feed
            
            # Display the texture on the Image widget
            self.image_widget.texture = texture

    def toggle_camera(self, instance):
        # Release the current capture
        self.capture.release()
        
        # Toggle the camera index
        self.camera_index = 1 - self.camera_index  # Switch between 0 and 1
        
        # Re-initialize the capture with the new camera index
        self.capture = cv2.VideoCapture(self.camera_index)

    def on_stop(self):
        # Release the camera when the app stops
        self.capture.release()


if __name__ == "__main__":
    CameraToggleApp().run()