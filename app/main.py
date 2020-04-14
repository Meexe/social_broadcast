import dispatchers.vk_api as vk
import dispatchers.fb_api as fb
from settings import settings

result = vk.post(settings['vk_token'], settings['vk_gid'], 'baca')
print(result)
result = fb.post(settings['fb_token'], settings['fb_gid'], 'baca')
print(result)
