# EYE MOUSE

<h3>숙명여자대학교 인공지능학과 오픈소스프로그래밍 팀프로젝트;</h3> <br>
<p style= " color: gray; text-decoration : underline;" >개발기간: 5월 2주 ~ 6월 2주 </p>

<h2>주제:</h2>
안구 움직임을 이용한 마우스 (Eye Mouse)
<h3>기대효과:</h3>
신체적인 제약이 있는 사람들에게 자유로운 컴퓨터 사용을 가능하게 함.

<h3>기능:</h3> 
1. 실시간 눈 추적: 웹캠을 사용하여 실시간으로 눈 움직임을 추적합니다.<br>
2. 마우스 커서 제어: 눈의 위치를 기반으로 마우스 커서를 이동시킵니다.<br>
3. 클릭 이벤트 감지: 눈 깜빡임을 감지하여 마우스 클릭 이벤트를 발생시킵니다.<br>
4. 감도 조절: 사용자가 GUI를 통해 커서 이동의 감도를 조절할 수 있습니다.

<h3>프로젝트 사전 요구 사항:</h3>
1. Python 3.x <br>
2. OpenCV <br>
3. MediaPipe <br>
4. PyAutoGUI<br>
5. Tkinter (Python 표준 라이브러리)<br>

<h3>프로젝트 실행방법:</h3>
1.프로젝트를 클론하거나 다운로드합니다.<br>
2.필요한 라이브러리를 설치합니다.<br>
3.eye_controlled_mouse.py 파일을 실행합니다<br>
4.Tkinter GUI 창이 나타나면 "Start" 버튼을 클릭하여 눈 제어 마우스를 시작합니다.<br>
5.감도 버튼을 사용하여 커서 이동 감도를 조절할 수 있습니다.<br>
6.프로그램을 종료하려면 창을 닫거나 'q' 키를 누릅니다.<br>

<h3>코드 설명:</h3>
<h4>주요 함수 및 클래스</h4>
1.start_eye_controlled_mouse(): 웹캠을 통해 실시간으로 프레임을 캡처하고, MediaPipe를 사용하여 얼굴 랜드마크를 탐지하여 마우스 커서를 제어합니다.<br>
2. on_closing(): 창을 닫을 때 사용자에게 확인 메시지를 표시하고, 사용자가 종료를 확인하면 프로그램을 종료합니다.<br>
3. check_stop_condition(): 주기적으로 stop_thread 플래그를 체크하여 프로그램을 종료합니다.<br>
4. start_thread(): start_eye_controlled_mouse 함수를 별도의 스레드에서 실행하여 메인 Tkinter 이벤트 루프와 분리합니다.<br>
5. update_scaling_factor(value): 커서 이동 감도를 업데이트하고, 라벨을 갱신합니다.
