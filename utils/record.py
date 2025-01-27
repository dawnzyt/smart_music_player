import wave

import numpy as np
import pyaudio


class RecordAudio:
    def __init__(self):
        # 录音参数
        self.chunk = 1024
        self.format = pyaudio.paInt16
        self.channels = 1
        self.rate = 16000

        # 打开录音
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.format,
                                  channels=self.channels,
                                  rate=self.rate,
                                  input=True,
                                  frames_per_buffer=self.chunk)

    def record(self,progress_bar, output_path="./otherFiles/temp.wav", record_seconds=3):
        """
        录音
        :param output_path: 录音保存的路径，后缀名为wav
        :param record_seconds: 录音时间，默认3秒
        :return: 录音的文件路径
        """

        frames = []
        for i in range(0, int(self.rate / self.chunk * record_seconds)):
            progress_bar.setValue(int(i/(self.rate / self.chunk * record_seconds)*100))
            data = self.stream.read(self.chunk)
            frames.append(data)
        progress_bar.setValue(100)
        print("录音已结束!")
        wf = wave.open(output_path, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.p.get_sample_size(self.format))
        wf.setframerate(self.rate)
        wf.writeframes(b''.join(frames))
        wf.close()
        return output_path