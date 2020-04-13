import dispatchers.vk_api as vk
from settings import settings

result = vk.post(settings['vk_token'], settings['vk_gid'], 'baca')
