import sys
import time
import numpy as np
from naoqi import ALProxy

start = time.time()

def main(robotIP, port, unit_time):
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.52, 1, 1.4, 2, 2.6, 3.2, 3.8, 4.4, 4.88, 5.48])
    keys.append([[-0.18719, [3, -0.173333, 0], [3, 0.16, 0]], [-0.185656, [3, -0.16, -0.00153415], [3, 0.133333, 0.00127846]], [0.0291041, [3, -0.133333, 0], [3, 0.2, 0]], [-0.185656, [3, -0.2, 0], [3, 0.2, 0]], [0.00149202, [3, -0.2, 0], [3, 0.2, 0]], [-0.185656, [3, -0.2, 0], [3, 0.2, 0]], [0.0812599, [3, -0.2, 0], [3, 0.2, 0]], [-0.185656, [3, -0.2, 0.080677], [3, 0.16, -0.0645416]], [-0.354396, [3, -0.16, 0], [3, 0.2, 0]], [-0.233211, [3, -0.2, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([0.52, 1, 1.4, 2, 2.6, 3.2, 3.8, 4.4, 4.88, 5.48])
    keys.append([[-0.00157595, [3, -0.173333, 0], [3, 0.16, 0]], [-0.00157595, [3, -0.16, 0], [3, 0.133333, 0]], [-0.00157595, [3, -0.133333, 0], [3, 0.2, 0]], [0.00609397, [3, -0.2, 0], [3, 0.2, 0]], [-4.19617e-05, [3, -0.2, 0], [3, 0.2, 0]], [0.00609397, [3, -0.2, 0], [3, 0.2, 0]], [-4.19617e-05, [3, -0.2, 0], [3, 0.2, 0]], [0.00609397, [3, -0.2, -0.00613594], [3, 0.16, 0.00490875]], [0.431013, [3, -0.16, 0], [3, 0.2, 0]], [-0.00924586, [3, -0.2, 0], [3, 0, 0]]])

    names.append("LAnklePitch")
    times.append([0.52, 1, 2.32, 4.4, 4.88, 5.48])
    keys.append([[0.105804, [3, -0.173333, 0], [3, 0.16, 0]], [-0.417291, [3, -0.16, 0.0634053], [3, 0.44, -0.174365]], [-0.607505, [3, -0.44, 0], [3, 0.693333, 0]], [-0.421891, [3, -0.693333, 0], [3, 0.16, 0]], [-0.671934, [3, -0.16, 0], [3, 0.2, 0]], [0.108872, [3, -0.2, 0], [3, 0, 0]]])

    names.append("LAnkleRoll")
    times.append([0.52, 1, 2.32, 4.4, 4.88, 5.48])
    keys.append([[-0.0735901, [3, -0.173333, 0], [3, 0.16, 0]], [-0.0858622, [3, -0.16, 0.00463609], [3, 0.44, -0.0127492]], [-0.125746, [3, -0.44, 0], [3, 0.693333, 0]], [-0.0858622, [3, -0.693333, 0], [3, 0.16, 0]], [-0.105804, [3, -0.16, 0.00409066], [3, 0.2, -0.00511333]], [-0.113474, [3, -0.2, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([0.52, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.88, 5.48])
    keys.append([[-0.435615, [3, -0.173333, 0], [3, 0.16, 0]], [-1.24863, [3, -0.16, 0], [3, 0.0666667, 0]], [-1.07529, [3, -0.0666667, -0.0429523], [3, 0.0666667, 0.0429523]], [-0.990921, [3, -0.0666667, 0], [3, 0.0666667, 0]], [-1.4005, [3, -0.0666667, 0.0922825], [3, 0.0666667, -0.0922825]], [-1.54462, [3, -0.0666667, 0], [3, 0.0666667, 0]], [-1.39897, [3, -0.0666667, -0.0493303], [3, 0.0666667, 0.0493303]], [-1.24863, [3, -0.0666667, -0.0539458], [3, 0.0666667, 0.0539458]], [-1.07529, [3, -0.0666667, -0.0429523], [3, 0.0666667, 0.0429523]], [-0.990921, [3, -0.0666667, 0], [3, 0.0666667, 0]], [-1.4005, [3, -0.0666667, 0.0922825], [3, 0.0666667, -0.0922825]], [-1.54462, [3, -0.0666667, 0], [3, 0.0666667, 0]], [-1.39897, [3, -0.0666667, -0.0493303], [3, 0.0666667, 0.0493303]], [-1.24863, [3, -0.0666667, -0.0539458], [3, 0.0666667, 0.0539458]], [-1.07529, [3, -0.0666667, -0.0429523], [3, 0.0666667, 0.0429523]], [-0.990921, [3, -0.0666667, 0], [3, 0.0666667, 0]], [-1.4005, [3, -0.0666667, 0.0922825], [3, 0.0666667, -0.0922825]], [-1.54462, [3, -0.0666667, 0], [3, 0.0666667, 0]], [-1.39897, [3, -0.0666667, 0], [3, 0.16, 0]], [-1.53856, [3, -0.16, 0], [3, 0.2, 0]], [-0.446352, [3, -0.2, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([0.52, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.88, 5.48])
    keys.append([[-1.21344, [3, -0.173333, 0], [3, 0.16, 0]], [-0.434165, [3, -0.16, -0.21079], [3, 0.0666667, 0.0878291]], [-0.31758, [3, -0.0666667, -0.0449974], [3, 0.0666667, 0.0449974]], [-0.16418, [3, -0.0666667, -0.0631497], [3, 0.0666667, 0.0631497]], [0.061318, [3, -0.0666667, -0.0590701], [3, 0.0666667, 0.0590701]], [0.190241, [3, -0.0666667, 0], [3, 0.0666667, 0]], [-0.176453, [3, -0.0666667, 0.104068], [3, 0.0666667, -0.104068]], [-0.434165, [3, -0.0666667, 0], [3, 0.0666667, 0]], [-0.31758, [3, -0.0666667, -0.0447418], [3, 0.0666667, 0.0447418]], [-0.165714, [3, -0.0666667, -0.0631497], [3, 0.0666667, 0.0631497]], [0.061318, [3, -0.0666667, -0.0593258], [3, 0.0666667, 0.0593258]], [0.190241, [3, -0.0666667, 0], [3, 0.0666667, 0]], [-0.176453, [3, -0.0666667, 0.104068], [3, 0.0666667, -0.104068]], [-0.434165, [3, -0.0666667, 0], [3, 0.0666667, 0]], [-0.31758, [3, -0.0666667, -0.0449974], [3, 0.0666667, 0.0449974]], [-0.16418, [3, -0.0666667, -0.0631497], [3, 0.0666667, 0.0631497]], [0.061318, [3, -0.0666667, -0.0590701], [3, 0.0666667, 0.0590701]], [0.190241, [3, -0.0666667, 0], [3, 0.0666667, 0]], [-0.176453, [3, -0.0666667, 0.172657], [3, 0.16, -0.414376]], [-1.57086, [3, -0.16, 0], [3, 0.2, 0]], [-1.19503, [3, -0.2, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([0.52, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.88, 5.48])
    keys.append([[0.3136, [3, -0.173333, 0], [3, 0.16, 0]], [0, [3, -0.16, 0], [3, 0.0666667, 0]], [0.1872, [3, -0.0666667, -0.000799999], [3, 0.0666667, 0.000799999]], [0.188, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.184, [3, -0.0666667, 0.00399999], [3, 0.0666667, -0.00399999]], [0, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.1908, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.1872, [3, -0.0666667, -0.000799999], [3, 0.0666667, 0.000799999]], [0.188, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.184, [3, -0.0666667, 0.00399999], [3, 0.0666667, -0.00399999]], [0, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.1908, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.1872, [3, -0.0666667, -0.000799999], [3, 0.0666667, 0.000799999]], [0.188, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.184, [3, -0.0666667, 0.00399999], [3, 0.0666667, -0.00399999]], [0, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.1908, [3, -0.0666667, -0.0980392], [3, 0.16, 0.235294]], [1, [3, -0.16, 0], [3, 0.2, 0]], [0.2976, [3, -0.2, 0], [3, 0, 0]]])

    names.append("LHipPitch")
    times.append([0.52, 1, 2.32, 4.4, 4.88, 5.48])
    keys.append([[0.131966, [3, -0.173333, 0], [3, 0.16, 0]], [-0.052114, [3, -0.16, 0.0414521], [3, 0.44, -0.113993]], [-0.33437, [3, -0.44, 0], [3, 0.693333, 0]], [-0.052114, [3, -0.693333, 0], [3, 0.16, 0]], [-0.406468, [3, -0.16, 0], [3, 0.2, 0]], [0.144238, [3, -0.2, 0], [3, 0, 0]]])

    names.append("LHipRoll")
    times.append([0.52, 1, 2.32, 4.4, 4.88, 5.48])
    keys.append([[0.06447, [3, -0.173333, 0], [3, 0.16, 0]], [0.1335, [3, -0.16, -0.00981766], [3, 0.44, 0.0269986]], [0.174919, [3, -0.44, 0], [3, 0.693333, 0]], [0.131966, [3, -0.693333, 0], [3, 0.16, 0]], [0.276162, [3, -0.16, 0], [3, 0.2, 0]], [0.115092, [3, -0.2, 0], [3, 0, 0]]])

    names.append("LHipYawPitch")
    times.append([0.52, 1, 2.32, 4.4, 4.88, 5.48])
    keys.append([[-0.170232, [3, -0.173333, 0], [3, 0.16, 0]], [-0.36505, [3, -0.16, 0.0050202], [3, 0.44, -0.0138056]], [-0.378855, [3, -0.44, 0], [3, 0.693333, 0]], [-0.36505, [3, -0.693333, 0], [3, 0.16, 0]], [-0.371186, [3, -0.16, 0], [3, 0.2, 0]], [-0.171766, [3, -0.2, 0], [3, 0, 0]]])

    names.append("LKneePitch")
    times.append([0.52, 1, 2.32, 4.4, 4.88, 5.48])
    keys.append([[-0.0874801, [3, -0.173333, 0], [3, 0.16, 0]], [0.731677, [3, -0.16, -0.108539], [3, 0.44, 0.298482]], [1.13358, [3, -0.44, 0], [3, 0.693333, 0]], [0.730143, [3, -0.693333, 0], [3, 0.16, 0]], [1.30079, [3, -0.16, 0], [3, 0.2, 0]], [-0.092082, [3, -0.2, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([0.52, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.88, 5.48])
    keys.append([[1.4818, [3, -0.173333, 0], [3, 0.16, 0]], [0.357381, [3, -0.16, 0], [3, 0.0666667, 0]], [0.510779, [3, -0.0666667, -0.0378384], [3, 0.0666667, 0.0378384]], [0.584411, [3, -0.0666667, -0.0158514], [3, 0.0666667, 0.0158514]], [0.605888, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.101229, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.282215, [3, -0.0666667, -0.0426919], [3, 0.0666667, 0.0426919]], [0.357381, [3, -0.0666667, -0.0380941], [3, 0.0666667, 0.0380941]], [0.510779, [3, -0.0666667, -0.0378384], [3, 0.0666667, 0.0378384]], [0.584411, [3, -0.0666667, -0.0158514], [3, 0.0666667, 0.0158514]], [0.605888, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.101229, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.282215, [3, -0.0666667, -0.0426919], [3, 0.0666667, 0.0426919]], [0.357381, [3, -0.0666667, -0.0380941], [3, 0.0666667, 0.0380941]], [0.510779, [3, -0.0666667, -0.0378384], [3, 0.0666667, 0.0378384]], [0.584411, [3, -0.0666667, -0.0158514], [3, 0.0666667, 0.0158514]], [0.605888, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.101229, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.282215, [3, -0.0666667, 0], [3, 0.16, 0]], [0.095066, [3, -0.16, 0], [3, 0.2, 0]], [1.4726, [3, -0.2, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([0.52, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.88, 5.48])
    keys.append([[0.0797259, [3, -0.173333, 0], [3, 0.16, 0]], [0.159494, [3, -0.16, 0], [3, 0.0666667, 0]], [0.141086, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.151824, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.0889301, [3, -0.0666667, 0.0404302], [3, 0.0666667, -0.0404302]], [-0.0907571, [3, -0.0666667, 0], [3, 0.0666667, 0]], [-0.066004, [3, -0.0666667, -0.0247531], [3, 0.0666667, 0.0247531]], [0.159494, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.141086, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.151824, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.0889301, [3, -0.0666667, 0.0404302], [3, 0.0666667, -0.0404302]], [-0.0907571, [3, -0.0666667, 0], [3, 0.0666667, 0]], [-0.066004, [3, -0.0666667, -0.0247531], [3, 0.0666667, 0.0247531]], [0.159494, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.141086, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.151824, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.0889301, [3, -0.0666667, 0.0404302], [3, 0.0666667, -0.0404302]], [-0.0907571, [3, -0.0666667, 0], [3, 0.0666667, 0]], [-0.066004, [3, -0.0666667, -0.0247531], [3, 0.16, 0.0594075]], [0.466294, [3, -0.16, 0], [3, 0.2, 0]], [0.12728, [3, -0.2, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([0.52, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.88, 5.48])
    keys.append([[-0.213269, [3, -0.173333, 0], [3, 0.16, 0]], [-0.573758, [3, -0.16, 0.0945665], [3, 0.0666667, -0.0394027]], [-0.615176, [3, -0.0666667, 0], [3, 0.0666667, 0]], [-0.412688, [3, -0.0666667, -0.0700526], [3, 0.0666667, 0.0700526]], [-0.194861, [3, -0.0666667, 0], [3, 0.0666667, 0]], [-0.961676, [3, -0.0666667, 0], [3, 0.0666667, 0]], [-0.763974, [3, -0.0666667, -0.0646531], [3, 0.0666667, 0.0646531]], [-0.573758, [3, -0.0666667, 0], [3, 0.0666667, 0]], [-0.615176, [3, -0.0666667, 0], [3, 0.0666667, 0]], [-0.412688, [3, -0.0666667, -0.0700526], [3, 0.0666667, 0.0700526]], [-0.194861, [3, -0.0666667, 0], [3, 0.0666667, 0]], [-0.961676, [3, -0.0666667, 0], [3, 0.0666667, 0]], [-0.763974, [3, -0.0666667, -0.0646531], [3, 0.0666667, 0.0646531]], [-0.573758, [3, -0.0666667, 0], [3, 0.0666667, 0]], [-0.615176, [3, -0.0666667, 0], [3, 0.0666667, 0]], [-0.411154, [3, -0.0666667, -0.0700526], [3, 0.0666667, 0.0700526]], [-0.194861, [3, -0.0666667, 0], [3, 0.0666667, 0]], [-0.961676, [3, -0.0666667, 0], [3, 0.0666667, 0]], [-0.763974, [3, -0.0666667, 0], [3, 0.16, 0]], [-1.79483, [3, -0.16, 0], [3, 0.2, 0]], [0.0843279, [3, -0.2, 0], [3, 0, 0]]])

    names.append("RAnklePitch")
    times.append([0.52, 1, 2.32, 4.4, 4.88, 5.48])
    keys.append([[0.0951499, [3, -0.173333, 0], [3, 0.16, 0]], [-0.31136, [3, -0.16, 0.016177], [3, 0.44, -0.0444867]], [-0.355846, [3, -0.44, 0], [3, 0.693333, 0]], [-0.31136, [3, -0.693333, 0], [3, 0.16, 0]], [-0.443284, [3, -0.16, 0], [3, 0.2, 0]], [0.105888, [3, -0.2, 0], [3, 0, 0]]])

    names.append("RAnkleRoll")
    times.append([0.52, 1, 2.32, 4.4, 4.88, 5.48])
    keys.append([[0.122762, [3, -0.173333, 0], [3, 0.16, 0]], [0.124296, [3, -0.16, -0.00153397], [3, 0.44, 0.00421842]], [0.144238, [3, -0.44, 0], [3, 0.693333, 0]], [0.124296, [3, -0.693333, 0], [3, 0.16, 0]], [0.314512, [3, -0.16, 0], [3, 0.2, 0]], [0.073674, [3, -0.2, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([0.52, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.88, 5.48])
    keys.append([[0.385075, [3, -0.173333, 0], [3, 0.16, 0]], [1.33309, [3, -0.16, -0.0331333], [3, 0.0666667, 0.0138056]], [1.34689, [3, -0.0666667, -0.0138056], [3, 0.0666667, 0.0138056]], [1.43126, [3, -0.0666667, 0], [3, 0.0666667, 0]], [1.31468, [3, -0.0666667, 0.0999658], [3, 0.0666667, -0.0999658]], [0.83147, [3, -0.0666667, 0], [3, 0.0666667, 0]], [1.16281, [3, -0.0666667, -0.083603], [3, 0.0666667, 0.083603]], [1.33309, [3, -0.0666667, -0.0138056], [3, 0.0666667, 0.0138056]], [1.34689, [3, -0.0666667, -0.0138056], [3, 0.0666667, 0.0138056]], [1.43126, [3, -0.0666667, 0], [3, 0.0666667, 0]], [1.31468, [3, -0.0666667, 0.0999658], [3, 0.0666667, -0.0999658]], [0.83147, [3, -0.0666667, 0], [3, 0.0666667, 0]], [1.16281, [3, -0.0666667, -0.083603], [3, 0.0666667, 0.083603]], [1.33309, [3, -0.0666667, -0.0138056], [3, 0.0666667, 0.0138056]], [1.34689, [3, -0.0666667, -0.0138056], [3, 0.0666667, 0.0138056]], [1.43126, [3, -0.0666667, 0], [3, 0.0666667, 0]], [1.31468, [3, -0.0666667, 0.0999658], [3, 0.0666667, -0.0999658]], [0.83147, [3, -0.0666667, 0], [3, 0.0666667, 0]], [1.16281, [3, -0.0666667, 0], [3, 0.16, 0]], [0.932714, [3, -0.16, 0.108857], [3, 0.2, -0.136071]], [0.428028, [3, -0.2, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([0.52, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.88, 5.48])
    keys.append([[1.23176, [3, -0.173333, 0], [3, 0.16, 0]], [0.185572, [3, -0.16, 0.0994033], [3, 0.0666667, -0.041418]], [0.144154, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.174835, [3, -0.0666667, -0.0306808], [3, 0.0666667, 0.0306808]], [0.351244, [3, -0.0666667, -0.0452529], [3, 0.0666667, 0.0452529]], [0.446352, [3, -0.0666667, 0], [3, 0.0666667, 0]], [-0.036858, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.185572, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.144154, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.176367, [3, -0.0666667, -0.0322132], [3, 0.0666667, 0.0322132]], [0.351244, [3, -0.0666667, -0.0449975], [3, 0.0666667, 0.0449975]], [0.446352, [3, -0.0666667, 0], [3, 0.0666667, 0]], [-0.036858, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.185572, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.144154, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.174835, [3, -0.0666667, -0.0306808], [3, 0.0666667, 0.0306808]], [0.351244, [3, -0.0666667, -0.0452529], [3, 0.0666667, 0.0452529]], [0.446352, [3, -0.0666667, 0], [3, 0.0666667, 0]], [-0.036858, [3, -0.0666667, 0.0819637], [3, 0.16, -0.196713]], [-0.389678, [3, -0.16, 0], [3, 0.2, 0]], [1.17347, [3, -0.2, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([0.52, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.88, 5.48])
    keys.append([[0.3112, [3, -0.173333, 0], [3, 0.16, 0]], [0, [3, -0.16, 0], [3, 0.0666667, 0]], [0.1568, [3, -0.0666667, -0.0212], [3, 0.0666667, 0.0212]], [0.178, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.1616, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.1672, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.1668, [3, -0.0666667, 0.000399992], [3, 0.0666667, -0.000399992]], [0, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.1568, [3, -0.0666667, -0.0212], [3, 0.0666667, 0.0212]], [0.178, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.1616, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.1672, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.1668, [3, -0.0666667, 0.000399992], [3, 0.0666667, -0.000399992]], [0, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.1568, [3, -0.0666667, -0.0212], [3, 0.0666667, 0.0212]], [0.178, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.1616, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.1672, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.1668, [3, -0.0666667, 0], [3, 0.16, 0]], [1, [3, -0.16, 0], [3, 0.2, 0]], [0.3044, [3, -0.2, 0], [3, 0, 0]]])

    names.append("RHipPitch")
    times.append([0.52, 1, 2.32, 4.4, 4.88, 5.48])
    keys.append([[0.139552, [3, -0.173333, 0], [3, 0.16, 0]], [-0.0767419, [3, -0.16, 0.0522242], [3, 0.44, -0.143617]], [-0.44797, [3, -0.44, 0], [3, 0.693333, 0]], [-0.0798099, [3, -0.693333, 0], [3, 0.16, 0]], [-0.104354, [3, -0.16, 0], [3, 0.2, 0]], [0.136484, [3, -0.2, 0], [3, 0, 0]]])

    names.append("RHipRoll")
    times.append([0.52, 1, 2.32, 4.4, 4.88, 5.48])
    keys.append([[-0.116542, [3, -0.173333, 0], [3, 0.16, 0]], [-0.128814, [3, -0.16, 0], [3, 0.44, 0]], [-0.108872, [3, -0.44, 0], [3, 0.693333, 0]], [-0.128814, [3, -0.693333, 0.0199421], [3, 0.16, -0.00460203]], [-0.208583, [3, -0.16, 0], [3, 0.2, 0]], [-0.0628521, [3, -0.2, 0], [3, 0, 0]]])

    names.append("RHipYawPitch")
    times.append([0.52, 1, 2.32, 4.4, 4.88, 5.48])
    keys.append([[-0.170232, [3, -0.173333, 0], [3, 0.16, 0]], [-0.36505, [3, -0.16, 0.0050202], [3, 0.44, -0.0138056]], [-0.378855, [3, -0.44, 0], [3, 0.693333, 0]], [-0.36505, [3, -0.693333, 0], [3, 0.16, 0]], [-0.371186, [3, -0.16, 0], [3, 0.2, 0]], [-0.171766, [3, -0.2, 0], [3, 0, 0]]])

    names.append("RKneePitch")
    times.append([0.52, 1, 2.32, 4.4, 4.88, 5.48])
    keys.append([[-0.0858622, [3, -0.173333, 0], [3, 0.16, 0]], [0.653526, [3, -0.16, -0.0969488], [3, 0.44, 0.266609]], [1.00481, [3, -0.44, 0], [3, 0.693333, 0]], [0.650458, [3, -0.693333, 0], [3, 0.16, 0]], [0.856014, [3, -0.16, 0], [3, 0.2, 0]], [-0.091998, [3, -0.2, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([0.52, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.88, 5.48])
    keys.append([[1.46808, [3, -0.173333, 0], [3, 0.16, 0]], [0.624379, [3, -0.16, 0], [3, 0.0666667, 0]], [0.744032, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.510865, [3, -0.0666667, 0.0723538], [3, 0.0666667, -0.0723538]], [0.309909, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.61671, [3, -0.0666667, -0.0692858], [3, 0.0666667, 0.0692858]], [0.725624, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.624379, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.744032, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.510865, [3, -0.0666667, 0.0723538], [3, 0.0666667, -0.0723538]], [0.309909, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.61671, [3, -0.0666667, -0.0692858], [3, 0.0666667, 0.0692858]], [0.725624, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.624379, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.744032, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.510865, [3, -0.0666667, 0.0723538], [3, 0.0666667, -0.0723538]], [0.309909, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.61671, [3, -0.0666667, -0.0692858], [3, 0.0666667, 0.0692858]], [0.725624, [3, -0.0666667, 0], [3, 0.16, 0]], [0.72409, [3, -0.16, 0], [3, 0.2, 0]], [1.46501, [3, -0.2, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([0.52, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.88, 5.48])
    keys.append([[-0.067538, [3, -0.173333, 0], [3, 0.16, 0]], [-0.0337899, [3, -0.16, -0.033748], [3, 0.0666667, 0.0140617]], [0.164096, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.124212, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.182504, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.0843279, [3, -0.0666667, 0.0217316], [3, 0.0666667, -0.0217316]], [0.052114, [3, -0.0666667, 0.0196863], [3, 0.0666667, -0.0196863]], [-0.0337899, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.164096, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.124212, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.182504, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.0843279, [3, -0.0666667, 0.0217316], [3, 0.0666667, -0.0217316]], [0.052114, [3, -0.0666667, 0.0196863], [3, 0.0666667, -0.0196863]], [-0.0337899, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.164096, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.124212, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.182504, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.0843279, [3, -0.0666667, 0.0217316], [3, 0.0666667, -0.0217316]], [0.052114, [3, -0.0666667, 0.027221], [3, 0.16, -0.0653305]], [-0.193327, [3, -0.16, 0], [3, 0.2, 0]], [-0.0767419, [3, -0.2, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([0.52, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.88, 5.48])
    keys.append([[-0.10282, [3, -0.173333, 0], [3, 0.16, 0]], [0.421808, [3, -0.16, 0], [3, 0.0666667, 0]], [0.409536, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.46476, [3, -0.0666667, -0.0127834], [3, 0.0666667, 0.0127834]], [0.486237, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.472429, [3, -0.0666667, 0.0138073], [3, 0.0666667, -0.0138073]], [0.131882, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.421808, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.409536, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.46476, [3, -0.0666667, -0.0127834], [3, 0.0666667, 0.0127834]], [0.486237, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.472429, [3, -0.0666667, 0.0138073], [3, 0.0666667, -0.0138073]], [0.131882, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.421808, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.409536, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.46476, [3, -0.0666667, -0.0127834], [3, 0.0666667, 0.0127834]], [0.486237, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.472429, [3, -0.0666667, 0.0138073], [3, 0.0666667, -0.0138073]], [0.131882, [3, -0.0666667, 0], [3, 0.16, 0]], [0.581345, [3, -0.16, 0], [3, 0.2, 0]], [0.118076, [3, -0.2, 0], [3, 0, 0]]])

    mul = unit_time/5.56
    times_unit = [list(np.array(t, dtype=float)*mul) for t in times]

    try:
        motion = ALProxy("ALMotion", robotIP, port)
        motion.angleInterpolationBezier(names, times_unit, keys)
    except BaseException, err:
        print err

if __name__ == "__main__":
    robotIP = "127.0.0.1" #"192.168.1.11"
    port = 9559 # Insert NAO port

    if len(sys.argv) <= 1:
        print "(robotIP default: 127.0.0.1)"
    elif len(sys.argv) <= 2:
        robotIP = sys.argv[1]
    else:
        port = int(sys.argv[2])
        robotIP = sys.argv[1]

    unit_time = float(sys.argv[3])

    main(robotIP, port, unit_time)

end = time.time()
print(end-start)
