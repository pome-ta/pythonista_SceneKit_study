from objc_util import load_framework, ObjCClass, ObjCInstance, on_main_thread, CGRect
import ui
import pdbg

load_framework('SceneKit')

class SceneView:
  @on_main_thread
  def __init__(self):
    self.SCNScene = ObjCClass('SCNScene')
    self.SCNView = ObjCClass('SCNView')
    
    self.view_did_load()

  def view_did_load(self):
    # --- View
    frame = CGRect((0, 0), (100, 100))
    flex_w, flex_h = (1 << 1), (1 << 4)
    self.scn_view = self.SCNView.alloc()
    self.scn_view.initWithFrame_options_(frame, None)
    #self.scn_view.autorelease()
    self.scn_view.autoresizingMask = (flex_w | flex_h)
    self.scn_view.allowsCameraControl = True
    self.scn_view.showsStatistics = True

    scene = self.SCNScene.new()
    self.scn_view.scene = scene


class View(ui.View):
  def __init__(self, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    self.bg_color = 'maroon'
    self.instance = ObjCInstance(self)
    scn = SceneView()
    self.instance.addSubview_(scn.scn_view)


if __name__ == '__main__':
  view = View()
  view.present(style='fullscreen', orientations=['portrait'])
