import shutil
import os

source_dir = os.path.join('C:', 'Users', 'username', 'Pictures')

destination_dir = os.path.join('C:', 'Users', 'username', 'Desktop')

shutil.copy2(os.path.join(source_dir, 'photo.jpg'), destination_dir)

