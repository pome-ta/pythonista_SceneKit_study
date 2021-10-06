from objc_util import load_framework, ObjCClass, ObjCInstance, on_main_thread
import ui
#import pdbg

load_framework('SceneKit')

SCNView = ObjCClass('SCNView')
SCNScene = ObjCClass('SCNScene')
SCNNode = ObjCClass('SCNNode')
SCNCamera = ObjCClass('SCNCamera')
SCNLight = ObjCClass('SCNLight')
SCNBox = ObjCClass('SCNBox')

UIColor = ObjCClass('UIColor')


class SceneView:
  @on_main_thread
  def __init__(self):
    self.view = self.create_view()
    self.view_did_load()

  def create_view(self):
    scnView = SCNView.alloc()
    scnView.initWithFrame_options_(((0, 0), (100, 100)), None)
    #self.scnView.autorelease()
    scnView.autoresizingMask = ((1 << 1) | (1 << 4))
    scnView.backgroundColor = UIColor.blackColor()
    scnView.allowsCameraControl = True
    scnView.showsStatistics = True
    '''
    OptionNone = 0
    ShowPhysicsShapes = (1 << 0)
    ShowBoundingBoxes = (1 << 1)
    ShowLightInfluences = (1 << 2)
    ShowLightExtents = (1 << 3)
    ShowPhysicsFields = (1 << 4)
    ShowWireframe = (1 << 5)
    RenderAsWireframe = (1 << 6)
    ShowSkeletons = (1 << 7)
    ShowCreases = (1 << 8)
    ShowConstraints = (1 << 9)
    ShowCameras = (1 << 10)
    '''
    scnView.debugOptions = (1 << 1) | (1 << 3) | (1 << 5) | (1 << 6) | (1 << 10)
    return scnView

  def view_did_load(self):
    scene = SCNScene.scene()

    cameraNode = SCNNode.node()
    cameraNode.camera = SCNCamera.camera()
    cameraNode.position = (0.0, 0.0, 25.0)
    scene.rootNode().addChildNode_(cameraNode)

    box = SCNBox.box()
    box.width = 1
    box.height = 1
    box.length = 1
    boxNode = SCNNode.node()
    boxNode.geometry = box
    scene.rootNode().addChildNode_(boxNode)

    self.view.scene = scene


class View(ui.View):
  def __init__(self, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    self.bg_color = 'maroon'
    self.instance = ObjCInstance(self)
    scn = SceneView()
    self.instance.addSubview_(scn.view)


if __name__ == '__main__':
  view = View()
  view.present(style='fullscreen', orientations=['portrait'])

