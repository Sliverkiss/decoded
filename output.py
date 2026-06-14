# Decoded from obfuscated Python (marshal+zlib+base85)
# Code object name: <module>
# Top-level names: ('base64', 'hashlib', 'hmac', 'json', 'os', 'random', 'string', 'threading', 'time', 'uuid', 'concurrent.futures', 'ThreadPoolExecutor', 'as_completed', 'datetime', 'requests', 'requests.adapters', 'HTTPAdapter', 'urllib3.util.retry', 'Retry', 'RPC_URL', 'COOKIE_ENV', 'HTTP_TIMEOUT', 'REQUEST_INTERVAL', 'DRAW_INTERVAL_RANGE', 'ACCOUNT_INTERVAL', 'PROGRESS_REFRESH_DELAY', 'int', 'getenv', 'DEFAULT_THREADS', 'DISCLAIMER', 'SERVER_NAME', 'ADD_TIMES_METHOD', 'AD_VIEWED_METHOD', 'LOTTERY_INFO_METHOD', 'LOTTERY_PROGRESS_METHOD', 'LOTTERY_METHOD', 'RECEIVE_EXTRA_LOTTERY_METHOD', 'IS_SHOW_STEP_LOTTERY_METHOD', 'AD_VIEWED_SIGN_KEY', 'ALREADY_DONE_TEXTS', 'ORDER_TASK_KEYWORDS', 'TASKS', 'tuple', 'FALLBACK_TASK_TYPES', 'TASK_NAME_BY_TYPE', 'AD_BUS_TYPE_BY_TASK', '_C', '_ACC_COLORS', 'Lock', '_print_lock', 'ts_print', 'colored', 'pick_int', 'pick_text', 'md5', 'build_retry_adapter', 'format_progress', 'can_attempt_progress_reward', 'describe_prize', 'is_finished_task', 'is_order_task', 'is_already_done_message', 'configured_task_types', 'configured_skip_types', 'parse_int_list', 'walk_task_tree', 'looks_like_task', 'XiaocanLotteryBot', '_run_one_account', 'main', '__name__')
# Varnames: ()

import os, sys, time, random, hashlib, platform, requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from sys import stdout, reconfigure

# ===== Constants =====
BASE_URL = "https://gwh.xiaocantech.com/rpc"
APP_ID = 20
# xcplus
# XC_THREADS
# 免责声明：本脚本仅供学习和接口调试使用，请遵守平台规则和相关法律法规；所发布的内容仅供学习，禁止用于其他用途，您必须在下载后的24小时内从计算机或手机中完全删除以上内容。严禁产生利益链！一旦使用或复制
# SilkwormLottery
# SilkwormLotteryMobile.AddLotteryTimes
# SilkwormLotteryMobile.OnAdViewed
# SilkwormLotteryMobile.LotteryInfo
# SilkwormLotteryMobile.GetLotteryProgress
# SilkwormLotteryMobile.Lottery
# SilkwormLotteryMobile.ReceiveExtraLottery
# SilkwormLotteryMobile.IsShowStepLottery
# lcjkbqadfrzsewxy
# if_shared
# 领取美团红包
# is_get_meituan_redpack
# 领取饿了么红包
# is_get_eleme_redpack
# 浏览福利页
# is_view_welfare_page
# 浏览霸王餐页面
# is_view_bwc_page
# 看视频得抽奖机会
# is_view_tp_ad
# 浏览抖音商城
# is_view_douyin_mall
# [31m
# [32m
# [33m
# [34m
# [36m
# [35m
# [90m
# [2m
# [1m
# [0m
# XiaocanLotteryBot
# __main__

# ===== Bytecode Structure =====
=== Code: <module> ===
  file: <__>
  names: ('base64', 'hashlib', 'hmac', 'json', 'os', 'random', 'string', 'threading', 'time', 'uuid', 'concurrent.futures', 'ThreadPoolExecutor', 'as_completed', 'datetime', 'requests', 'requests.adapters', 'HTTPAdapter', 'urllib3.util.retry', 'Retry', 'RPC_URL', 'COOKIE_ENV', 'HTTP_TIMEOUT', 'REQUEST_INTERVAL', 'DRAW_INTERVAL_RANGE', 'ACCOUNT_INTERVAL', 'PROGRESS_REFRESH_DELAY', 'int', 'getenv', 'DEFAULT_THREADS', 'DISCLAIMER', 'SERVER_NAME', 'ADD_TIMES_METHOD', 'AD_VIEWED_METHOD', 'LOTTERY_INFO_METHOD', 'LOTTERY_PROGRESS_METHOD', 'LOTTERY_METHOD', 'RECEIVE_EXTRA_LOTTERY_METHOD', 'IS_SHOW_STEP_LOTTERY_METHOD', 'AD_VIEWED_SIGN_KEY', 'ALREADY_DONE_TEXTS', 'ORDER_TASK_KEYWORDS', 'TASKS', 'tuple', 'FALLBACK_TASK_TYPES', 'TASK_NAME_BY_TYPE', 'AD_BUS_TYPE_BY_TASK', '_C', '_ACC_COLORS', 'Lock', '_print_lock', 'ts_print', 'colored', 'pick_int', 'pick_text', 'md5', 'build_retry_adapter', 'format_progress', 'can_attempt_progress_reward', 'describe_prize', 'is_finished_task', 'is_order_task', 'is_already_done_message', 'configured_task_types', 'configured_skip_types', 'parse_int_list', 'walk_task_tree', 'looks_like_task', 'XiaocanLotteryBot', '_run_one_account', 'main', '__name__')
  varnames: ()
  constants (89):
    [0] 0
    [2] ('ThreadPoolExecutor', 'as_completed')
    [3] ('datetime',)
    [4] ('HTTPAdapter',)
    [5] ('Retry',)
    [6] 'https://gwh.xiaocantech.com/rpc'
    [7] 'xcplus'
    [8] 15
    [9] 2
    [10] (5, 10)
    [11] 20
    [12] 'XC_THREADS'
    [13] '3'
    [14] '免责声明：本脚本仅供学习和接口调试使用，请遵守平台规则和相关法律法规；所发布的内容仅供学习，禁止用于其他用途，您必须在下载后的24小时内从计算机或手机中完全删除以上内容。严禁产生利益链！一旦使用或复制了任何相关脚本或Script项目的规则，'
    [15] 'SilkwormLottery'
    [16] 'SilkwormLotteryMobile.AddLotteryTimes'
    [17] 'SilkwormLotteryMobile.OnAdViewed'
    [18] 'SilkwormLotteryMobile.LotteryInfo'
    [19] 'SilkwormLotteryMobile.GetLotteryProgress'
    [20] 'SilkwormLotteryMobile.Lottery'
    [21] 'SilkwormLotteryMobile.ReceiveExtraLottery'
    [22] 'SilkwormLotteryMobile.IsShowStepLottery'
    [23] 'lcjkbqadfrzsewxy'
    [24] ('已完成', '已经完成', '限一次', '今日已')
    [25] ('下单', '订单', '支付', '购买', 'order', 'pay')
    [26] 1
    [27] '签到'
    [28] ('type', 'name')
    [29] '分享'
    [30] 'if_shared'
    [31] ('type', 'name', 'flag')
    [32] 8
    [33] '领取美团红包'
    [34] 'is_get_meituan_redpack'
    [35] 9
    [36] '领取饿了么红包'
    [37] 'is_get_eleme_redpack'
    [38] 10
    [39] '浏览福利页'
    [40] 'is_view_welfare_page'
    [41] 11
    [42] '浏览霸王餐页面'
    [43] 'is_view_bwc_page'
    [44] 6
    [45] '看视频得抽奖机会'
    [46] 'is_view_tp_ad'
    [47] ('type', 'name', 'flag', 'bus_type')
    [48] 7
    [49] '浏览抖音商城'
    [50] 'is_view_douyin_mall'
    [51] 4
    [52] <code <genexpr>>
    [53] <code <dictcomp>>
    [54] <code <dictcomp>>
    [55] '\x1b[31m'
    [56] '\x1b[32m'
    [57] '\x1b[33m'
    [58] '\x1b[34m'
    [59] '\x1b[36m'
    [60] '\x1b[35m'
    [61] '\x1b[90m'
    [62] '\x1b[2m'
    [63] '\x1b[1m'
    [64] '\x1b[0m'
    [65] ('R', 'G', 'Y', 'B', 'C', 'M', 'W', 'D', 'BOLD', 'RST')
    [66] ('B', 'M', 'C', 'G', 'R', 'Y')
    [67] <code ts_print>
    [68] <code colored>
    [69] <code pick_int>
    [70] <code pick_text>
    [71] <code md5>
    [72] <code build_retry_adapter>
    [73] <code format_progress>
    [74] <code can_attempt_progress_reward>
    [75] <code describe_prize>
    [76] <code is_finished_task>
    [77] <code is_order_task>
    [78] <code is_already_done_message>
    [79] <code configured_task_types>
    [80] <code configured_skip_types>
    [81] <code parse_int_list>
    [82] <code walk_task_tree>
    [83] <code looks_like_task>
    [84] <code XiaocanLotteryBot>
    [85] 'XiaocanLotteryBot'
    [86] <code _run_one_account>
    [87] <code main>
    [88] '__main__'

  === Code: <genexpr> ===
    file: <__>
    names: ()
    varnames: ('.0', 'task')
    constants (2):
      [0] 'type'

  === Code: <dictcomp> ===
    file: <__>
    names: ()
    varnames: ('.0', 'task')
    constants (2):
      [0] 'type'
      [1] 'name'

  === Code: <dictcomp> ===
    file: <__>
    names: ()
    varnames: ('.0', 'task')
    constants (2):
      [0] 'bus_type'
      [1] 'type'

  === Code: ts_print ===
    file: <__>
    names: ('_print_lock', 'print')
    varnames: ('args', 'kwargs')
    constants (1):

  === Code: colored ===
    file: <__>
    names: ('join', '_C')
    varnames: ('text', 'codes', 'prefix')
    constants (4):
      [1] ''
      [2] <code <genexpr>>
      [3] 'RST'

    === Code: <genexpr> ===
      file: <__>
      names: ('_C', 'get')
      varnames: ('.0', 'c')
      constants (2):
        [0] ''

  === Code: pick_int ===
    file: <__>
    names: ('isinstance', 'dict', 'get', 'bool', 'int', 'str', 'isdigit')
    varnames: ('data', 'keys', 'key', 'value')
    constants (1):

  === Code: pick_text ===
    file: <__>
    names: ('isinstance', 'dict', 'get', 'str', 'strip')
    varnames: ('data', 'keys', 'key', 'value')
    constants (2):
      [1] ''

  === Code: md5 ===
    file: <__>
    names: ('hashlib', 'md5', 'encode', 'hexdigest')
    varnames: ('text',)
    constants (1):

  === Code: build_retry_adapter ===
    file: <__>
    names: ('Retry', 'frozenset', 'HTTPAdapter')
    varnames: ('retry',)
    constants (7):
      [1] 2
      [2] 0.5
      [3] (429, 500, 502, 503, 504)
      [4] 'POST'
      [5] ('total', 'connect', 'read', 'backoff_factor', 'status_forcelist', 'allowed_methods')
      [6] ('max_retries',)

  === Code: format_progress ===
    file: <__>
    names: ('str',)
    varnames: ('lottery_count', 'second_step_count')
    constants (2):
      [1] '/'

  === Code: can_attempt_progress_reward ===
    file: <__>
    names: ('get', 'isinstance', 'int', 'bool')
    varnames: ('reward', 'threshold', 'claimed')
    constants (4):
      [1] 'threshold'
      [2] 'claimed'
      [3] 0

  === Code: describe_prize ===
    file: <__>
    names: ('isinstance', 'dict', 'pick_text')
    varnames: ('prize', 'default_name')
    constants (2):
      [1] ('name', 'prize_name', 'goods_name', 'title')

  === Code: is_finished_task ===
    file: <__>
    names: ('get', 'join', 'strip')
    varnames: ('task', 'status_text')
    constants (10):
      [1] 'raw'
      [2] 'is_finished'
      [3] True
      [4] 'finished'
      [5] ''
      [6] <code <genexpr>>
      [7] ('status_text', 'task_status_text', 'button_text', 'state_text')
      [8] '已完成'
      [9] '完成'

    === Code: <genexpr> ===
      file: <__>
      names: ('str', 'get')
      varnames: ('.0', 'key')
      constants (2):
        [0] ''

  === Code: is_order_task ===
    file: <__>
    names: ('any', 'ORDER_TASK_KEYWORDS')
    varnames: ('task_name',)
    constants (2):
      [1] <code <genexpr>>

    === Code: <genexpr> ===
      file: <__>
      names: ('lower',)
      varnames: ('.0', 'keyword')
      constants (1):

  === Code: is_already_done_message ===
    file: <__>
    names: ('any', 'ALREADY_DONE_TEXTS')
    varnames: ('message',)
    constants (2):
      [1] <code <genexpr>>

    === Code: <genexpr> ===
      file: <__>
      names: ('str',)
      varnames: ('.0', 'text')
      constants (1):

  === Code: configured_task_types ===
    file: <__>
    names: ('os', 'getenv', 'FALLBACK_TASK_TYPES', 'parse_int_list', 'tuple')
    varnames: ('value', 'task_types')
    constants (3):
      [1] 'XC_TASK_TYPES'
      [2] ''

  === Code: configured_skip_types ===
    file: <__>
    names: ('set', 'parse_int_list', 'os', 'getenv')
    varnames: ()
    constants (3):
      [1] 'XC_SKIP_TASK_TYPES'
      [2] ''

  === Code: parse_int_list ===
    file: <__>
    names: ('replace', 'split')
    varnames: ('value',)
    constants (4):
      [1] <code <listcomp>>
      [2] '，'
      [3] ','

    === Code: <listcomp> ===
      file: <__>
      names: ('strip', 'isdigit', 'int')
      varnames: ('.0', 'item')
      constants (0):

  === Code: walk_task_tree ===
    file: <__>
    names: ('isinstance', 'dict', 'pick_int', 'pick_text', 'looks_like_task', 'append', 'get', 'values', 'walk_task_tree', 'list')
    varnames: ('value', 'tasks', 'task_type', 'task_name', 'child', 'item')
    constants (6):
      [1] ('task_type', 'type')
      [2] ('task_name', 'task_title', 'title', 'name', 'desc', 'task_desc')
      [3] 'task_status'
      [4] 'status'
      [5] ('type', 'name', 'status', 'raw')

  === Code: looks_like_task ===
    file: <__>
    names: ('any',)
    varnames: ('value',)
    constants (3):
      [1] <code <genexpr>>
      [2] ('task_type', 'task_status', 'task_name', 'task_title', 'lottery_count_add', 'lottery_times')

    === Code: <genexpr> ===
      file: <__>
      names: ()
      varnames: ('.0', 'key')
      constants (1):

  === Code: XiaocanLotteryBot ===
    file: <__>
    names: ('__name__', '__module__', '__qualname__', '__init__', '_log', '_kv', '_section', 'staticmethod', 'parse_cookie', 'build_base_headers', 'refresh_auth_headers', 'base_payload', 'silk_id_as_int', 'rpc', 'fetch_lottery_info', 'extract_tasks', 'task_from_config', 'complete_tasks', 'complete_regular_task', 'complete_ad_task', '_print_task_result', 'build_ad_payload', 'fetch_draw_count', 'draw_all_prizes', 'draw_once', 'fetch_lottery_progress', 'can_receive_progress_rewards', 'receive_progress_rewards', 'receive_progress_reward', 'run')
    varnames: ()
    constants (33):
      [0] 'XiaocanLotteryBot'
      [1] ''
      [2] 'C'
      [3] <code __init__>
      [4] <code _log>
      [5] True
      [6] <code _kv>
      [7] <code _section>
      [8] <code parse_cookie>
      [9] <code build_base_headers>
      [10] <code refresh_auth_headers>
      [11] <code base_payload>
      [12] <code silk_id_as_int>
      [13] <code rpc>
      [14] <code fetch_lottery_info>
      [15] <code extract_tasks>
      [16] <code task_from_config>
      [17] <code complete_tasks>
      [18] <code complete_regular_task>
      [19] <code complete_ad_task>
      [20] <code _print_task_result>
      [21] <code build_ad_payload>
      [22] <code fetch_draw_count>
      [23] <code draw_all_prizes>
      [24] <code draw_once>
      [25] <code fetch_lottery_progress>
      [26] <code can_receive_progress_rewards>
      [27] <code receive_progress_rewards>
      [28] <code receive_progress_reward>
      [29] <code run>
      [31] ('', 'C')
      [32] (True,)

    === Code: __init__ ===
      file: <__>
      names: ('parse_cookie', 'user_id', 'silk_id', 'token', 'label', 'cc', 'requests', 'Session', 'session', 'mount', 'build_retry_adapter', 'build_base_headers', 'headers', 'success')
      varnames: ('self', 'cookie', 'account_label', 'color_code', 'user_id', 'silk_id', 'token')
      constants (3):
        [1] 'https://'
        [2] True

    === Code: _log ===
      file: <__>
      names: ('colored', 'label', 'cc', 'ts_print')
      varnames: ('self', 'args', 'prefix')
      constants (4):
        [1] '['
        [2] ']'
        [3] 'BOLD'

    === Code: _kv ===
      file: <__>
      names: ('_log', 'colored', 'cc', 'str')
      varnames: ('self', 'key', 'value', 'ok', 'color')
      constants (4):
        [1] 'G'
        [2] 'R'
        [3] '  '

    === Code: _section ===
      file: <__>
      names: ('_log', 'colored', 'cc')
      varnames: ('self', 'title')
      constants (3):
        [1] '┌─ '
        [2] ' ─────────────────────────────────────┐'

    === Code: parse_cookie ===
      file: <__>
      names: ('strip', 'split', 'len', 'ValueError', 'isdigit')
      varnames: ('cookie', 'parts')
      constants (8):
        [1] '#'
        [2] 3
        [3] 'cookie 格式应为: x-vayne#x-teemo#x-sivir'
        [4] 0
        [5] 1
        [6] 2
        [7] 'cookie 内容无效'

    === Code: build_base_headers ===
      file: <__>
      names: ('user_id', 'silk_id', 'token', 'SERVER_NAME', 'LOTTERY_METHOD')
      varnames: ('self',)
      constants (31):
        [1] 'Host'
        [2] 'gwh.xiaocantech.com'
        [3] 'x-version'
        [4] '3.4.5'
        [5] 'x-vayne'
        [6] 'x-platform'
        [7] 'mini'
        [8] 'x-annie'
        [9] 'XC'
        [10] 'x-city'
        [11] '430100'
        [12] 'x-nami'
        [13] ''
        [14] 'x-teemo'
        [15] 'x-garen'
        [16] 'x-sivir'
        [17] 'x-ashe'
        [18] 'servername'
        [19] 'methodname'
        [20] 'content-type'
        [21] 'application/json'
        [22] 'accept'
        [23] 'application/json, text/plain, */*'
        [24] 'origin'
        [25] 'https://gw.djtaoke.cn'
        [26] 'referer'
        [27] 'https://gw.djtaoke.cn/'
        [28] 'com.tencent.mm'
        [29] 'Mozilla/5.0 (Linux; Android 13; 23054RA19C Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0'
        [30] ('x-requested-with', 'user-agent')

    === Code: refresh_auth_headers ===
      file: <__>
      names: ('uuid', 'uuid4', 'hex', 'max', 'len', 'silk_id', 'str', 'int', 'time', 'SERVER_NAME', 'lower', 'md5', 'headers', 'update')
      varnames: ('self', 'method_name', 'request_id', 'random_tail_length', 'x_nami', 'x_garen', 'service_method', 'x_ashe')
      constants (7):
        [1] 0
        [2] 20
        [3] 4
        [4] 1000
        [5] '.'
        [6] ('methodname', 'x-nami', 'x-garen', 'x-ashe')

    === Code: base_payload ===
      file: <__>
      names: ('silk_id_as_int', 'update')
      varnames: ('self', 'extra', 'payload')
      constants (2):
        [1] 'silk_id'

    === Code: silk_id_as_int ===
      file: <__>
      names: ('int', 'silk_id')
      varnames: ('self',)
      constants (1):

    === Code: rpc ===
      file: <__>
      names: ('refresh_auth_headers', 'json', 'dumps', 'session', 'post', 'RPC_URL', 'headers', 'HTTP_TIMEOUT', 'raise_for_status', 'ValueError', 'isinstance', 'dict')
      varnames: ('self', 'method_name', 'data', 'payload', 'response', 'result', 'exc')
      constants (6):
        [1] (',', ':')
        [2] ('separators',)
        [3] ('headers', 'data', 'timeout')
        [4] '接口返回不是合法 JSON: '
        [5] '接口返回格式异常: '

    === Code: fetch_lottery_info ===
      file: <__>
      names: ('rpc', 'LOTTERY_INFO_METHOD', 'base_payload', 'get', '_kv')
      varnames: ('self', 'response', 'status')
      constants (10):
        [1] 'status'
        [2] 'code'
        [3] 0
        [4] '任务'
        [5] '获取失败 ['
        [6] 'msg'
        [7] ']'
        [8] False
        [9] ('ok',)

    === Code: extract_tasks ===
      file: <__>
      names: ('isinstance', 'dict', 'get', 'TASKS', 'walk_task_tree')
      varnames: ('self', 'response', 'tasks')
      constants (3):
        [1] 'lottery_info'
        [2] <code <listcomp>>

      === Code: <listcomp> ===
        file: <__>
        names: ('task_from_config',)
        varnames: ('.0', 'config')
        constants (0):

    === Code: task_from_config ===
      file: <__>
      names: ('get', 'bool')
      varnames: ('config', 'lottery_info', 'flag', 'is_finished')
      constants (7):
        [1] 'flag'
        [2] False
        [3] 'type'
        [4] 'name'
        [5] ('is_finished', 'task_name', 'task_type')
        [6] ('type', 'name', 'status', 'raw')

    === Code: complete_tasks ===
      file: <__>
      names: ('_section', 'extract_tasks', 'fetch_lottery_info', '_kv', 'configured_task_types', 'len', 'set', 'configured_skip_types', 'get', 'TASK_NAME_BY_TYPE', 'add', 'is_order_task', 'is_finished_task', 'AD_BUS_TYPE_BY_TASK', 'complete_ad_task', 'complete_regular_task', 'success', 'requests', 'RequestException', 'time', 'sleep', 'REQUEST_INTERVAL')
      varnames: ('self', 'tasks', 'handled_types', 'skipped_types', 'task', 'task_type', 'task_name', 'ok', 'exc')
      constants (17):
        [1] '任务'
        [2] '未获取到明细，使用兜底列表'
        [3] <code <listcomp>>
        [4] '发现 '
        [5] ' 个'
        [6] 'type'
        [7] 'name'
        [8] ''
        [9] '任务['
        [10] ']'
        [11] '：跳过下单任务'
        [12] '：已完成，跳过'
        [13] False
        [14] '] '
        [15] '请求异常 ['
        [16] ('ok',)

      === Code: <listcomp> ===
        file: <__>
        names: ('TASK_NAME_BY_TYPE', 'get')
        varnames: ('.0', 'task_type')
        constants (2):
          [0] ''
          [1] ('type', 'name', 'raw')

    === Code: complete_regular_task ===
      file: <__>
      names: ('base_payload', 'int', 'rpc', 'ADD_TIMES_METHOD', '_print_task_result')
      varnames: ('self', 'task_type', 'task_name', 'data', 'response')
      constants (3):
        [1] 'type'
        [2] ()

    === Code: complete_ad_task ===
      file: <__>
      names: ('rpc', 'AD_VIEWED_METHOD', 'build_ad_payload', '_print_task_result')
      varnames: ('self', 'task_type', 'task_name', 'bus_type', 'response')
      constants (1):

    === Code: _print_task_result ===
      file: <__>
      names: ('get', '_kv', 'str', 'is_already_done_message')
      varnames: ('self', 'task_type', 'task_name', 'response', 'status', 'name', 'message')
      constants (15):
        [0] '返回 True=成功(含已完成), False=真正失败'
        [1] 'status'
        [2] ' '
        [3] ''
        [4] 'code'
        [5] 0
        [6] '任务['
        [7] ']'
        [8] '：完成'
        [9] True
        [10] 'msg'
        [11] '：已完成，跳过'
        [12] '：失败 ['
        [13] False
        [14] ('ok',)

    === Code: build_ad_payload ===
      file: <__>
      names: ('int', 'time', 'join', 'range', 'silk_id_as_int', 'hmac', 'new', 'AD_VIEWED_SIGN_KEY', 'encode', 'hashlib', 'sha256', 'digest', 'base_payload', 'base64', 'b64encode', 'decode')
      varnames: ('self', 'bus_type', 'timestamp', 'nonce', 'sign_text', 'signature')
      constants (9):
        [1] ''
        [2] <code <genexpr>>
        [3] 6
        [4] 'silk_id='
        [5] '&timestamp='
        [6] '&nonce='
        [7] '&bus_type='
        [8] ('timestamp', 'nonce', 'bus_type', 'sign')

      === Code: <genexpr> ===
        file: <__>
        names: ('random', 'choice', 'string', 'ascii_lowercase')
        varnames: ('.0', '_')
        constants (1):

    === Code: fetch_draw_count ===
      file: <__>
      names: ('fetch_lottery_info', 'pick_int', 'get')
      varnames: ('self', 'info', 'count')
      constants (5):
        [1] 'lottery_info'
        [2] ('day_num',)
        [3] ('lucky_times',)
        [4] 0

    === Code: draw_all_prizes ===
      file: <__>
      names: ('_section', 'fetch_draw_count', '_kv', 'draw_once', 'time', 'sleep', 'random', 'randint', 'DRAW_INTERVAL_RANGE')
      varnames: ('self', 'draw_count', 'drawn_count', 'prize_name')
      constants (11):
        [1] '抽奖'
        [2] 0
        [3] '无可用次数'
        [4] False
        [5] ('ok',)
        [6] '可用 '
        [7] ' 次'
        [8] 1
        [9] '获得 ['
        [10] ']，剩余 '

    === Code: draw_once ===
      file: <__>
      names: ('rpc', 'LOTTERY_METHOD', 'base_payload', 'get', 'str', '_kv')
      varnames: ('self', 'response', 'status', 'message', 'prize')
      constants (18):
        [1] 1
        [2] ('prize_type',)
        [3] 'status'
        [4] 'code'
        [5] 0
        [6] 'msg'
        [7] '无抽奖次数'
        [8] '抽奖'
        [9] '次数已用完'
        [10] False
        [11] ('ok',)
        [12] '失败 ['
        [13] ']'
        [14] ''
        [15] 'prize'
        [16] 'name'
        [17] '未知奖品'

    === Code: fetch_lottery_progress ===
      file: <__>
      names: ('rpc', 'LOTTERY_PROGRESS_METHOD', 'base_payload', 'get', '_kv')
      varnames: ('self', 'response', 'status')
      constants (11):
        [1] 'status'
        [2] 'code'
        [3] 0
        [4] '奖励'
        [5] '进度获取失败 ['
        [6] 'msg'
        [7] ']'
        [8] False
        [9] ('ok',)
        [10] 'lottery_progress'

    === Code: can_receive_progress_rewards ===
      file: <__>
      names: ('rpc', 'IS_SHOW_STEP_LOTTERY_METHOD', 'base_payload', 'get', '_kv', 'isinstance', 'bool')
      varnames: ('self', 'response', 'status', 'show')
      constants (11):
        [1] 'status'
        [2] 'code'
        [3] 0
        [4] '奖励'
        [5] '资格判断失败 ['
        [6] 'msg'
        [7] ']'
        [8] False
        [9] ('ok',)
        [10] 'show'

    === Code: receive_progress_rewards ===
      file: <__>
      names: ('_section', 'can_receive_progress_rewards', '_kv', 'fetch_lottery_progress', 'pick_int', 'format_progress', 'get', 'can_attempt_progress_reward', 'bool', 'receive_progress_reward', 'time', 'sleep', 'REQUEST_INTERVAL')
      varnames: ('self', 'can_receive', 'progress', 'lottery_count', 'first_step_count', 'second_step_count', 'rewards', 'has_ready_reward', 'reward')
      constants (26):
        [1] '进度奖励'
        [2] False
        [3] '奖励'
        [4] '当前账号暂无进度奖励领取资格，跳过'
        [5] ('lottery_count',)
        [6] 0
        [7] ('first_step_count',)
        [8] ('second_step_count',)
        [9] '当前进度 '
        [10] 1
        [11] 'has_got_first_step_prize'
        [12] '饭票'
        [13] ('step', 'threshold', 'claimed', 'name')
        [14] 2
        [15] 'has_got_second_step_prize'
        [16] '小蚕红包'
        [17] '奖励['
        [18] 'step'
        [19] ']'
        [20] 'name'
        [21] '：无可领取配置，跳过'
        [22] 'claimed'
        [23] 'threshold'
        [24] True
        [25] '暂无可领取进度奖励'

    === Code: receive_progress_reward ===
      file: <__>
      names: ('rpc', 'RECEIVE_EXTRA_LOTTERY_METHOD', 'base_payload', 'int', 'get', 'is_already_done_message', '_kv', 'describe_prize')
      varnames: ('self', 'step', 'default_name', 'response', 'status', 'message', 'prize', 'prize_name')
      constants (15):
        [1] ('step',)
        [2] 'status'
        [3] 'code'
        [4] 0
        [5] 'msg'
        [6] '奖励['
        [7] ']'
        [8] '：已领取'
        [9] '：领取失败 ['
        [10] False
        [11] ('ok',)
        [12] 'prize'
        [13] '领取成功 ['
        [14] True

    === Code: run ===
      file: <__>
      names: ('complete_tasks', 'draw_all_prizes', 'time', 'sleep', 'PROGRESS_REFRESH_DELAY', 'receive_progress_rewards')
      varnames: ('self', 'drawn_count')
      constants (1):

  === Code: _run_one_account ===
    file: <__>
    names: ('_ACC_COLORS', 'len', 'XiaocanLotteryBot', 'run', 'success', 'ValueError', 'requests', 'RequestException', '__new__', 'label', 'cc', '_kv', 'str')
    varnames: ('cookie', 'index', 'total', 'color', 'label', 'bot', 'exc')
    constants (8):
      [1] 1
      [2] '账号'
      [3] '/'
      [4] ('account_label', 'color_code')
      [5] '异常'
      [6] False
      [7] ('ok',)

  === Code: main ===
    file: <__>
    names: ('ts_print', 'colored', 'DISCLAIMER', 'os', 'getenv', 'COOKIE_ENV', 'strip', 'split', 'len', 'min', 'DEFAULT_THREADS', 'time', 'ThreadPoolExecutor', 'enumerate', 'as_completed', 'result', 'append', 'sort', 'sum', 'str')
    varnames: ('cookie_text', 'cookies', 'threads', 'start_time', 'results', 'futures', 'future', 'idx', 'success', 'error', 'elapsed', 'ok_count', 'fail_count', 'error_accounts')
    constants (28):
      [1] 'D'
      [2] ''
      [3] '请设置环境变量：'
      [4] 'R'
      [5] <code <listcomp>>
      [6] '@'
      [7] '=================================================='
      [8] 'C'
      [9] '  小蚕霸王餐 - 多账号并发执行'
      [10] 'BOLD'
      [11] '  线程数: '
      [12] '  |  账号数: '
      [13] ('max_workers',)
      [14] <code <dictcomp>>
      [15] <code <lambda>>
      [16] ('key',)
      [17] <code <genexpr>>
      [18] '  执行完成'
      [19] '  成功: '
      [20] 'G'
      [21] '  |  失败: '
      [22] '  |  总耗时: '
      [23] '.1f'
      [24] '秒'
      [25] <code <listcomp>>
      [26] '  账号'
      [27] ' 执行异常: '

    === Code: <listcomp> ===
      file: <__>
      names: ('strip',)
      varnames: ('.0', 'cookie')
      constants (0):

    === Code: <dictcomp> ===
      file: <__>
      names: ('submit', '_run_one_account')
      varnames: ('.0', 'i', 'cookie')
      constants (1):
        [0] 1

    === Code: <lambda> ===
      file: <__>
      names: ()
      varnames: ('x',)
      constants (2):
        [1] 0

    === Code: <genexpr> ===
      file: <__>
      names: ()
      varnames: ('.0', '_', 's')
      constants (2):
        [0] 1

    === Code: <listcomp> ===
      file: <__>
      names: ()
      varnames: ('.0', 'idx', '_', 'error')
      constants (0):

# Use the original decode logic to reconstruct manually
# or run this module with Python 3.12+ to execute directly.