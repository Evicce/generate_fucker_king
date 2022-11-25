import random

import pandas as pd
import datetime
import calendar
import uuid
import numpy as np

造当期 = False


def get_uuid():
    return str(uuid.uuid4()).replace('-', '')


def get_this_year_last_day():
    year = datetime.datetime.now().year
    if not 造当期:
        year = year - 1
    return str(year) + '-12-31'


def get_this_quarter_last_day():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    if not 造当期:
        month = month - 3
        if month == 0:
            year = year - 1
            month = 12

    if month <= 3:
        return str(year) + '-03-31'
    if month <= 6:
        return str(year) + '-06-30'
    if month <= 9:
        return str(year) + '-09-30'
    if month <= 12:
        return str(year) + '-12-31'


def get_this_month_last_day():
    # 获取当前年份
    year = datetime.date.today().year
    # 获取当前月份
    month = datetime.date.today().month
    if not 造当期:
        month = month - 1
        if month == 0:
            year = year - 1
            month = 12
    # 获取当前月的第一天的星期和当月总天数
    weekDay, monthCountDay = calendar.monthrange(year, month)
    # 获取当前月份最后一天
    lastDay = datetime.date(year, month, day=monthCountDay)
    # 返回第一天和最后一天
    return str(lastDay)


def get_this_day():
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    if not 造当期:
        yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
        return yesterday.strftime('%Y-%m-%d')
    return today


def handle_dt(s):
    if s['频率'] == 'Y':
        if pd.isna(s['历史期数']):
            s['具体日期'] = get_this_year_last_day()
        else:
            year = s['历史期数']
            s['具体日期'] = str(year) + '-12-31'
    if s['频率'] == 'Q':
        if pd.isna(s['历史期数']):
            s['具体日期'] = get_this_quarter_last_day()
        else:
            year = s['历史期数'].split('Q')[0]
            quarter = s['历史期数'].split('Q')[1]
            month = int(quarter) * 3
            if month == 3:
                s['具体日期'] = year + '-03-31'
            if month == 6:
                s['具体日期'] = year + '-06-30'
            if month == 9:
                s['具体日期'] = year + '-09-30'
            if month == 12:
                s['具体日期'] = year + '-12-31'
    if s['频率'] == 'M':
        if pd.isna(s['历史期数']):
            s['具体日期'] = get_this_month_last_day()
        else:
            year = s['历史期数'].split('/')[0]
            month = s['历史期数'].split('/')[1]
            if int(month) == 1:
                s['具体日期'] = year + '-01-31'
            if int(month) == 2:
                s['具体日期'] = year + '-02-28'
            if int(month) == 3:
                s['具体日期'] = year + '-03-31'
            if int(month) == 4:
                s['具体日期'] = year + '-04-30'
            if int(month) == 5:
                s['具体日期'] = year + '-05-31'
            if int(month) == 6:
                s['具体日期'] = year + '-06-30'
            if int(month) == 7:
                s['具体日期'] = year + '-07-31'
            if int(month) == 8:
                s['具体日期'] = year + '-08-31'
            if int(month) == 9:
                s['具体日期'] = year + '-09-30'
            if int(month) == 10:
                s['具体日期'] = year + '-10-31'
            if int(month) == 11:
                s['具体日期'] = year + '-11-30'
            if int(month) == 12:
                s['具体日期'] = year + '-12-31'
    if s['频率'] == 'D':
        if pd.isna(s['历史期数']):
            s['具体日期'] = get_this_day()
        else:
            s['具体日期'] = s['历史期数']

    return s


def generate_bl_ind_value(s):
    stat_dt = s['具体日期']
    rate = s['频率']
    branch_no = s['机构编号']
    branch_name = s['机构名称']
    curr_id = '1'
    indi_code = s['指标编号']
    page_name = s['页面']
    ass_name = s['模块']
    index_pro_name = s['指标中文（页面展示）']

    rate_ind_list = ['BL20220090',
                     'BL20220091',
                     'BL20220093',
                     'BL20220094',
                     'BL20220096',
                     'BL20220097',
                     'BL20220099',
                     'BL20220100',
                     'BL20220102',
                     'BL20220103',
                     'BL20220107',
                     'BL20220111',
                     'BL20220115',
                     'BL20220119',
                     'BL20220024',
                     'BL20220027',
                     'BL20220030',
                     'BL20220033',
                     'BL20220036'
                     ]
    if indi_code in rate_ind_list:

        curr_num = round(random.uniform(1, 100), 2)
        corr_num = round(random.uniform(1, 100), 2)
        last_num = round(random.uniform(1, 100), 2)
        yeat_begin_num = round(random.uniform(1, 100), 2)
    else:
        curr_num = random.randint(100000000, 999999999)
        corr_num = random.randint(100000000, 999999999)
        last_num = random.randint(100000000, 999999999)
        yeat_begin_num = random.randint(100000000, 999999999)
    year_add = random.randint(100000000, 999999999)
    last_add_num = random.randint(100000000, 999999999)
    yeat_begin_add_num = random.randint(100000000, 999999999)
    yrar_add_rate = round(random.uniform(1, 100), 2)
    last_add_rate = round(random.uniform(1, 100), 2)
    yeat_begin_add_rate = round(random.uniform(1, 100), 2)

    return 'INSERT INTO "input_9_admin_cockpit" ' \
           '("stat_dt", "rate", "branch_no", "branch_name", "curr_id", "indi_code", "page_name", "ass_name", "index_pro_name", ' \
           '"curr_num", "corr_num", "year_add", "yrar_add_rate", "last_num", "last_add_num", "last_add_rate", "yeat_begin_num", ' \
           '"yeat_begin_add_num", "yeat_begin_add_rate") VALUES ' \
           f"('{stat_dt}', '{rate}', '{branch_no}', '{branch_name}', '{curr_id}', '{indi_code}', '{page_name}', '{ass_name}', '{index_pro_name}', " \
           f"'{curr_num}', '{corr_num}', '{year_add}', '{yrar_add_rate}', '{last_num}', '{last_add_num}', '{last_add_rate}', '{yeat_begin_num}', " \
           f"'{yeat_begin_add_num}', '{yeat_begin_add_rate}');\n"


def generate_ind_value(s):
    ind_num, ind_nm, data_dt, ind_fre, acg_org_num, acg_org_nm = s['指标编号'], s['指标中文（页面展示）'], s['具体日期'], \
                                                                 s['频率'], s['机构编号'], s['机构名称']

    rate_ind_list = ['率',
                     'ROA',
                     'ROE',
                     '票据利差']
    # rslt_id
    # ind_num
    # ind_nm
    # data_dt
    # ind_fre
    # acg_org_num
    # acg_org_nm
    # ind_org_type
    # ind_ccy
    rslt_id = str(uuid.uuid4()).replace('-', '')
    # print(s['指标中文（页面展示）'])
    for key_val in rate_ind_list:
        if key_val in s['指标中文（页面展示）']:
            crn_term_val = random.uniform(1, 6)  # 值
            crspd_ped_val = random.uniform(1, 6)  # 值
            lst_term_val = random.uniform(1, 6)  # 值
            bm_val = random.uniform(1, 6)  # 值
            bq_val = random.uniform(1, 6)  # 值
            by_val = random.uniform(1, 6)  # 值

            yoy_incrmt = random.uniform(1, 6)  # 增量
            mom_incrmt = random.uniform(1, 6)  # 增量
            cbm_incrmt = random.uniform(1, 6)  # 增量
            cbq_incrmt = random.uniform(1, 6)  # 增量
            cby_incrmt = random.uniform(1, 6)  # 增量
            print(0)

        # if '价格' in s['页面中文']:
        #     crn_term_val = random.uniform(1, 6)  # 值
        #     crspd_ped_val = random.uniform(1, 6)  # 值
        #     lst_term_val = random.uniform(1, 6)  # 值
        #     bm_val = random.uniform(1, 6)  # 值
        #     bq_val = random.uniform(1, 6)  # 值
        #     by_val = random.uniform(1, 6)  # 值
        #
        #     yoy_incrmt = random.uniform(1, 6)  # 增量
        #     mom_incrmt = random.uniform(1, 6)  # 增量
        #     cbm_incrmt = random.uniform(1, 6)  # 增量
        #     cbq_incrmt = random.uniform(1, 6)  # 增量
        #     cby_incrmt = random.uniform(1, 6)  # 增量
        #     print(1)
        # elif '预算完成率' in s['指标中文（页面展示）']:
        #     crn_term_val = random.randint(10, 50)  # 值
        #     crspd_ped_val = random.randint(10, 50)  # 值
        #     lst_term_val = random.randint(10, 50)  # 值
        #     bm_val = random.randint(10, 50)  # 值
        #     bq_val = random.randint(10, 50)  # 值
        #     by_val = random.randint(10, 50)  # 值
        #
        #     yoy_incrmt = random.randint(10, 50)  # 增量
        #     mom_incrmt = random.randint(10, 50)  # 增量
        #     cbm_incrmt = random.randint(10, 50)  # 增量
        #     cbq_incrmt = random.randint(10, 50)  # 增量
        #     cby_incrmt = random.randint(10, 50)  # 增量
        #     print(2)
        #
        # elif '率' in s['指标中文（页面展示）']:
        #     crn_term_val = random.uniform(1, 6)  # 值
        #     crspd_ped_val = random.uniform(1, 6)  # 值
        #     lst_term_val = random.uniform(1, 6)  # 值
        #     bm_val = random.uniform(1, 6)  # 值
        #     bq_val = random.uniform(1, 6)  # 值
        #     by_val = random.uniform(1, 6)  # 值
        #
        #     yoy_incrmt = random.uniform(1, 6)  # 增量
        #     mom_incrmt = random.uniform(1, 6)  # 增量
        #     cbm_incrmt = random.uniform(1, 6)  # 增量
        #     cbq_incrmt = random.uniform(1, 6)  # 增量
        #     cby_incrmt = random.uniform(1, 6)  # 增量
        #     print(3)
        # elif '户' in s['指标中文（页面展示）']:
        #     crn_term_val = random.randint(1000, 4000)  # 值
        #     crspd_ped_val = random.randint(1000, 4000)  # 值
        #     lst_term_val = random.randint(1000, 4000)  # 值
        #     bm_val = random.randint(1000, 4000)  # 值
        #     bq_val = random.randint(1000, 4000)  # 值
        #     by_val = random.randint(1000, 4000)  # 值
        #
        #     yoy_incrmt = random.randint(1000, 4000)  # 增量
        #     mom_incrmt = random.randint(1000, 4000)  # 增量
        #     cbm_incrmt = random.randint(1000, 4000)  # 增量
        #     cbq_incrmt = random.randint(1000, 4000)  # 增量
        #     cby_incrmt = random.randint(1000, 4000)  # 增量
        #     print(4)
        else:
            crn_term_val = random.randint(1000000000, 300000000000)  # 值
            crspd_ped_val = random.randint(1000000000, 300000000000)  # 值
            lst_term_val = random.randint(1000000000, 300000000000)  # 值
            bm_val = random.randint(1000000000, 300000000000)  # 值
            bq_val = random.randint(1000000000, 300000000000)  # 值
            by_val = random.randint(1000000000, 300000000000)  # 值

            yoy_incrmt = random.randint(10000000, 3000000000)  # 增量
            mom_incrmt = random.randint(10000000, 3000000000)  # 增量
            cbm_incrmt = random.randint(10000000, 3000000000)  # 增量
            cbq_incrmt = random.randint(10000000, 3000000000)  # 增量
            cby_incrmt = random.randint(10000000, 3000000000)  # 增量
            print(5)
    yoy_incs = random.uniform(0, 100)  # 增幅
    mom_incs = random.uniform(0, 100)  # 增幅
    cbm_incr_rng = random.uniform(0, 100)  # 增幅
    cbq_incr_rng = random.uniform(0, 100)  # 增幅
    cby_incs = random.uniform(0, 100)  # 增幅

    return 'INSERT INTO "ind_indicator_result" ' \
           '("rslt_id", "ind_num", "ind_nm", "data_dt", "ind_fre", "acg_org_num", "acg_org_nm", ' \
           '"ind_org_type", "ind_ccy", "crn_term_val", "crspd_ped_val", "yoy_incrmt", "yoy_incs", ' \
           '"lst_term_val", "mom_incrmt", "mom_incs", "bm_val", "cbm_incrmt", "cbm_incr_rng", "bq_val", ' \
           '"cbq_incrmt", "cbq_incr_rng", "by_val", "cby_incrmt", "cby_incs", "spmt_val", "ov_inr_wrn_val_flag", "ov_regy_wrn_val_flag", "crt_empe_code", "crt_org_code", "crt_dt", "udt_empe_code", "udt_org_code", "udt_dt", "flag", "etl_dt", "is_additional_recording", "ie_kind_one_name", "ie_kind_two_name", "month_beginning_value") VALUES ' \
           f"('{rslt_id}', '{ind_num}', '{ind_nm}', '{data_dt}', '{ind_fre}', '{acg_org_num}', '{acg_org_nm}', " \
           f"'1', '1', '{crn_term_val}', '{crspd_ped_val}', '{yoy_incrmt}', '{yoy_incs}', " \
           f"'{lst_term_val}', '{mom_incrmt}', '{mom_incs}', '{bm_val}', '{cbm_incrmt}', '{cbm_incr_rng}', '{bq_val}', " \
           f"'{cbq_incrmt}', '{cbq_incr_rng}', '{by_val}', '{cby_incrmt}', '{cby_incs}', NULL, NULL, NULL, NULL, NULL, '2016-02-08 00:00:00', NULL, NULL, NULL, NULL, NULL, '1', NULL, NULL, NULL);\n"


def generate_ind_del_sql_BL(s):
    stat_dt = s['具体日期']
    indi_code = s['指标编号']
    rate = s['频率']
    return f"delete from input_9_admin_cockpit where stat_dt='{stat_dt}' and indi_code='{indi_code}' and rate='{rate}';\n"


def generate_ind_del_sql_JC(s):
    stat_dt = s['具体日期']
    indi_code = s['指标编号']
    rate = s['频率']
    return f"delete from ind_indicator_result where data_dt='{stat_dt}' and ind_num='{indi_code}' and ind_fre='{rate}';\n"


if __name__ == '__main__':
    df_ind = pd.read_excel(r"C:\Users\Evicce\Desktop\20221125导入\指标地图首页价格盈利LX.xlsx", sheet_name='盈利')
    df_area = pd.read_csv(r"C:\Users\Evicce\Desktop\20221125导入\区域.input")

    df_ind = df_ind[df_ind['指标编号'].str.contains('JC')]

    df_ind_res = df_ind.apply(handle_dt, axis=1)

    f = open(r"C:\Users\Evicce\Desktop\20221125导入\out_JC.sql", 'w+', encoding='utf-8')
    f_del = open(r"C:\Users\Evicce\Desktop\20221125导入\delete_JC.sql", 'w+', encoding='utf-8')
    for idx_ind, ind_s in df_ind_res.iterrows():
        for idx_area, area_s in df_area.iterrows():
            ind_s['机构编号'] = area_s['code']
            ind_s['机构名称'] = area_s['nm']
            sql = generate_ind_value(ind_s)
            sql_del = generate_ind_del_sql_JC(ind_s)
            f.write(sql)
            f_del.write(sql_del)

    f.close()
    f_del.close()
