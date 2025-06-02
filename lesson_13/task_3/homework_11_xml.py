import xml.etree.ElementTree as ET
import logging

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(console_handler)

# Завантаження XML-файлу
tree = ET.parse('groups.xml')
root = tree.getroot()

# Пошук елементу incoming у timingExbytes для кожної групи
for group in root.findall('group'):
    timing_exbytes = group.find('timingExbytes')
    if timing_exbytes is not None:
        incoming = timing_exbytes.find('incoming')
        if incoming is not None:
            logging.info(f"Group: {group.find('name').text}, incoming: {incoming.text}")
        else:
            logging.info(f"Group: {group.find('name').text}, incoming: Не знайдено")