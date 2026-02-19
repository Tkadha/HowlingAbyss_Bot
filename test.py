import fbx
manager = fbx.FbxManager.Create()
scene = fbx.FbxScene.Create(manager, "Scene")
importer = fbx.FbxImporter.Create(manager, "")

if importer.Initialize("your_file.fbx", -1, manager.GetIOSettings()):
    importer.Import(scene)
    print("Meshes:", scene.GetNodeCount())
    # 추가 분석 코드
importer.Destroy()