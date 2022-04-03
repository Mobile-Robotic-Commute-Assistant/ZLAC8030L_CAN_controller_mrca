"""
BSD 3-Clause License
Copyright (c) 2022, Mohamed Abdelkader Zahana
All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.
3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

"""
@brief This script tests getting the DC voltage of a particular node
"""

import logging
import  ZLAC8030L_CAN_controller.canopen_controller
from ZLAC8030L_CAN_controller.canopen_controller import MotorController
import time

node_ids = [1,2,3,4]
def main():
    logging.info("This scripts tests getting the DC voltage of a particular node \n")
    time.sleep(1)

    logging.info("Instantiating MotorController object ")
    obj = MotorController(channel='can0', bustype='socketcan_ctypes', bitrate=500000, node_ids=None, debug=True, eds_file='./eds/ZLAC8030L-V1.0.eds')

    for i in range(3):
        for node in node_ids:
            node=int(node)

            try:
                v_dict = obj.getVoltage(node)
                v = v_dict['value']
                logging.warn("Node {}: Voltage= {} V".format(node, v))
            except Exception as e:
                logging.error("Node {}: Could not read voltage. Error: {}".format(node, e))
        time.sleep(1)

    

    logging.info("Done instantiating. Disconnecting CAN network")
    obj.disconnectNetwork()
  

if __name__=="__main__":
    main()