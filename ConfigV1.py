"""
Created 1 july 2017
@author: mem
configuration for V1 chair
"""

"""
This file defines the coordinates of the upper (base) and lower (platform) attachment points
Note: because the chair is an inverted stewart platform, the base is the plane defined by the upper attachment points

The coordinate frame used follow ROS conventions, positive X is forward, positive Y us left, positive Z is up,
positive yaw is CCW from the persepective of person on the chair.

The origin is the center of the circle intersecting the attachment points. The X axis is the line through the origin running
 from back to front (X values increase moving from back to front). The Y axis passes through the origin with values increasing
 to the left.


 On the V1 platform the bottom front attachment points are closer to the origin than the other points,
 the bottom origin can be located with a plumb line from the top origin down to the lower platform.

The attachment coordinates can be specified explicitly or with vectors from the origin to
 each attachment point. Uncomment the desired method of entry.

You only need enter values for the left side, the other side is a mirror image and is calculated for you
"""
import math


PLATFORM_NAME = "Chair v1"

PLATFORM_UNLOADED_WEIGHT = 20  # weight of moving platform without 'passenger' in killograms
DEFAULT_PAYLOAD_WEIGHT = 65    # weight of 'passenger'
MAX_MUSCLE_LEN = 600           # length of muscle at minimum pressure
MIN_MUSCLE_LEN = MAX_MUSCLE_LEN * .75 # length of muscle at maximum pressure
FIXED_LEN = 200                #  length of fixing hardware
MIN_ACTUATOR_LEN = MIN_MUSCLE_LEN + FIXED_LEN  # total min actuator distance including fixing hardware
MAX_ACTUATOR_LEN = MAX_MUSCLE_LEN ++ FIXED_LEN # total max actuator distance including fixing hardware
MAX_ACTUATOR_RANGE = MAX_ACTUATOR_LEN - MIN_ACTUATOR_LEN
MID_ACTUATOR_LEN  = MIN_ACTUATOR_LEN + (MAX_ACTUATOR_RANGE/2)

DISABLED_LEN = 200 + MAX_MUSCLE_LEN *.99
WINDDOWN_LEN = MAX_ACTUATOR_LEN *.92  # not needed for V1 platform

"""
#uncomment this to define attachment locations using angles and distance from origin (vectors)
#only the left side is needed (as viewed facing the chair), the other side is calculated for you

#base attachment vectors
_baseAngles    = [65,70,178]   # enter angles from origin to attach point
_baseMagnitude = [650,645,650]

#Platform attachment vectors
_platformAngles    = [30,120,138]  # enter angles from origin to attach point
_platformMagnitude = [640,390,425] # enter distance from origin to attach point

#convert to radians and calculate x and y coordinates using sin and cos of angles
_baseAngles  = [math.radians(x) for x in _baseAngles]
base_pos     = [[m*math.cos(a),m*math.sin(a),0]  for a,m in zip(_baseAngles,_baseMagnitude)]

_platformAngles  = [math.radians(x) for x in _platformAngles]
platform_pos     = [[m*math.cos(a),m*math.sin(a),0]  for a,m in zip(_platformAngles,_platformMagnitude)]
"""

#  uncomment this to enter hard coded coordinates

#  input x and y coordinates with origin as center of the base plate
#  the z value should be zero for both base and platform
#  only left side is needed as other side is symmetrical
base_pos     = [
                 [171, 553, 0],  # first upper attachment point
                 [ 65, 555, 0],
                 [-691, 50, 0]
              ]

platform_pos = [
                [380, 260,  0 ],  # first lower attachment point
                [-222, 322,  0 ],
                [-330, 260,  0 ]
              ]

import numpy as np
base_pos_n = np.array(base_pos)
platform_pos_n = np.array(platform_pos)

#  print "\nPlatformOutput using %s configuration" %(PLATFORM_NAME)
#  print "Actuator lengths: Min %d, Max %d, mid %d" %( MIN_ACTUATOR_LEN, MAX_ACTUATOR_LEN, MID_ACTUATOR_LEN)

#  use actuator length and the distance between attachment points to calculate height extents
a = np.linalg.norm(base_pos_n[1]-platform_pos_n[1])  # distance between consecutive platform attachmment points

b = MID_ACTUATOR_LEN
platform_mid_height = math.sqrt(b * b - a * a)  # the mid vertical distance from center to fixed platform
platform_mid_height = -platform_mid_height;  # negative becuase this is an inverted stewart platform
print "mid height", round(platform_mid_height)

#  the range in mm or radians from origin to max extent in a single DOF 
platform_1dof_limits = [100, 122, 140, math.radians(15), math.radians(20), math.radians(8)]

# limits at extremes of movement
platform_6dof_limits = [75, 75, 80, math.radians(12), math.radians(12), math.radians(5)]

