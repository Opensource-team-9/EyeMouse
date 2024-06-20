Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "C:\oss\run_eye_controlled_mouse.bat" & Chr(34), 0
Set WshShell = Nothing
