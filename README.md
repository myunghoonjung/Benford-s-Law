# 벤포드의 법칙이란 ??

유튜브에서 **데이터 속에서 무작위로 뽑은 숫자의 첫 자리를 맞추는 게임**을 봤습니다. 게임의 규칙은 간단했어요. 1부터 9까지의 숫자 중 첫 자리가 뭐일지 맞추는 게임이었죠.

처음엔 당연히 **1부터 9까지 숫자가 고르게 분포**될 거라고 생각했어요. 그런데 결과는 이상했습니다. 숫자 **1**이 첫 번째 자리에 가장 많이 나타났고, 숫자 **9**는 가장 적게 나타났습니다. **왜 그럴까?** 그게 바로 **벤포드의 법칙**이었습니다. 신기하죠? 저도 스스로 정말 궁금해서 **코드로 직접 해보자**고 마음먹고, 급하게 자료를 찾아가며 구현해봤습니다.

## 결과
<img width="910" alt="스크린샷 2025-01-16 오전 8 22 00" src="https://github.com/user-attachments/assets/a713df91-083a-4f01-a8e2-3c885117a368" />

## 벤포드의 법칙이란?
간단히 말하면, 숫자의 첫 자리가 **1**일 확률이 가장 크고, **9**일 확률은 가장 적다는 법칙입니다. 예를 들어, 숫자가 **1**로 시작하는 경우가 훨씬 많고, **9**는 거의 나오지 않죠. 첫 자리가 1일 확률이 30%에 가깝습니다!

## 참고한 자료
계산 방법과 시각화 방법은 아래 링크를 참고하였습니다.
--아래--
(https://naysan.ca/2022/12/19/testing-benfords-law-using-python/)

## 참조 라이브러리
numpy, matplotlib 두개만 설치하시면 됩니다.
