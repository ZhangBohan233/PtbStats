import sys
import time

import xml_parser as psr
import ship_stats as ss


if __name__ == '__main__':
    st = time.time()
    # obj = psr.parse_file("Design61332/鱼雷测试艇.xml")

    ship = ss.ShipStats("Design61332/北卡.xml")
    print(ship.generate_report())
    print(time.time() - st)
