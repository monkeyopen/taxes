import datetime
import logging

# 初始化配置
# logging.basicConfig(format='%(filename)s:%(lineno)d - %(levelname)s: %(message)s', level=logging.DEBUG)
logging.basicConfig(format='%(filename)s:%(lineno)d - %(levelname)s: %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def str2float(str):
    if str == '':
        return 0
    else:
        return float(str.replace(",", ""))


class TaxData:
    # sell_list[0].code, sell_list[0].name, capital_gains, total_fee,
    #                        sell_list[0].currency
    def __init__(self, code, name, capital_gains, total_fee, currency):
        self.code = code
        self.name = name
        self.capital_gains = capital_gains
        self.total_fee = total_fee
        self.currency = currency

    def __str__(self):
        return (
            f"代码:{self.code}, 名称:{self.name}, 资本利润:{self.capital_gains}, 总费用:{self.total_fee}, 币种:{self.currency}")


class Data:
    # 代码	名称	方向	成交数量	成交价格	成交金额 成交时间	合计费用
    def __init__(self, code, name, direction, quantity, price, amount, time, fee, currency):
        self.code = code
        self.name = name
        self.direction = direction
        self.quantity = str2float(quantity)
        self.price = str2float(price)
        self.amount = str2float(amount)
        self.time = time
        self.fee = str2float(fee)
        self.currency = currency
        if self.direction == "买入":
            self.shares_held = self.quantity
        else:
            self.shares_held = self.quantity

    def __str__(self):
        return (
            f"代码:{self.code}, 名称:{self.name}, 方向:{self.direction}, 成交价格:{self.price}, 成交数量:{self.quantity}, 成交金额:{-self.amount if self.direction == '买入' else self.amount}, 成交时间:{self.time}, 合计费用:{self.fee}, 币种:{self.currency}, 持有数量:{self.shares_held}")


class ZongheData:
    # 代码	名称	方向	订单价格	订单数量	交易状态	已成交	下单时间	订单类型	订单来源	期限	时段	订单说明@订单组ID	盘前竞价	触发价	卖空	币种	市场	行权/指派	成交数量	成交价格	成交金额	对手经纪	成交时间	币种	市场	交易费	证监会规费	财汇局征费	平台使用费	印花税	交易活动费	综合审计跟踪监管费	证监会征费	佣金	交收费	合计费用	备注

    def __init__(self, code, name, direction, order_price, order_quantity, transaction_status, deal_quantity,
                 order_time,
                 order_type,
                 order_source, maturity, peiod, order_group_id, pre_bid, trigger_price, sell_empty, currency, market,
                 exercise_or_assign, deal_quantity2, deal_price, deal_amount, contra_broker, deal_time, currency2,
                 market2, trade_fee, supervision_fee, securities_fee, platform_fee, stamp_tax, trading_activity_fee,
                 cat_fee, sfc_fee, commission, settlement_fee, total_fee, remark):
        self.code = code
        self.name = name
        self.direction = direction
        self.order_price = order_price
        self.order_quantity = order_quantity
        self.transaction_status = transaction_status
        self.deal_quantity = deal_quantity
        self.order_time = order_time
        self.order_type = order_type
        self.order_source = order_source
        self.maturity = maturity
        self.peiod = peiod
        self.order_group_id = order_group_id
        self.pre_bid = pre_bid
        self.trigger_price = trigger_price
        self.sell_empty = sell_empty
        self.currency = currency
        self.market = market
        self.exercise_or_assign = exercise_or_assign
        self.deal_quantity2 = deal_quantity2
        self.deal_price = deal_price
        self.deal_amount = deal_amount
        self.contra_broker = contra_broker
        self.deal_time = deal_time
        self.currency2 = currency2
        self.market2 = market2
        self.trade_fee = trade_fee
        self.supervision_fee = supervision_fee
        self.securities_fee = securities_fee
        self.platform_fee = platform_fee
        self.stamp_tax = stamp_tax
        self.trading_activity_fee = trading_activity_fee
        self.cat_fee = cat_fee
        self.sfc_fee = sfc_fee
        self.commission = commission
        self.settlement_fee = settlement_fee
        self.total_fee = total_fee
        self.remark = remark

    def __str__(self):
        return (
            f"代码:{self.code}, 名称:{self.name}, 方向:{self.direction}, 订单价格:{self.order_price}, 订单数量:{self.order_quantity}, 交易状态:{self.transaction_status}, 已成交:{self.deal_quantity}, 下单时间:{self.order_time}, 订单类型:{self.order_type}, 订单来源:{self.order_source}, 期限:{self.maturity}, 时段:{self.peiod}, 订单说明:{self.order_group_id}, 盘前竞价:{self.pre_bid}, 触发价:{self.trigger_price}, 卖空:{self.sell_empty}, 币种:{self.currency}, 市场:{self.market}, 行权/指派:{self.exercise_or_assign}, 成交数量:{self.deal_quantity2}, 成交价格:{self.deal_price}, 成交金额:{self.deal_amount}, 对手经纪:{self.contra_broker}, 成交时间:{self.deal_time}, 币种:{self.currency2}, 市场:{self.market2}, 交易费:{self.trade_fee}, 证监会规费:{self.supervision_fee}, 财汇局征费:{self.securities_fee}, 平台使用费:{self.platform_fee}, 印花税:{self.stamp_tax}, 交易活动费:{self.trading_activity_fee}, 综合审计跟踪监管费:{self.cat_fee}, 证监会征费:{self.sfc_fee}, 佣金:{self.commission}, 交收费:{self.settlement_fee}, 合计费用:{self.total_fee}, 备注:{self.remark}")


class GangguData:
    # 代码	名称	方向	订单价格	订单数量	交易状态	已成交	下单时间	订单类型	订单来源	期限	盘前竞价	触发价	卖空	行权/指派	成交数量	成交价格	成交金额	对手经纪	成交时间	财汇局征费	证监会征费	平台使用费	交易费	交易系统使用费	交收费	交易征费	佣金	印花税	合计费用	备注

    def __init__(self, code, name, direction, order_price, order_quantity, transaction_status, deal_quantity,
                 order_time, order_type, order_source, maturity, pre_bid, trigger_price, sell_empty, exercise_or_assign,
                 deal_quantity2, deal_price, deal_amount, contra_broker, deal_time, securities_fee, supervision_fee,
                 platform_fee, transaction_fee, transaction_system_fee, settlement_fee, trade_fee, commission,
                 stamp_tax,
                 total_fee, remark):
        self.code = code
        self.name = name
        self.direction = direction
        self.order_price = order_price
        self.order_quantity = order_quantity
        self.transaction_status = transaction_status
        self.deal_quantity = deal_quantity
        self.order_time = order_time
        self.order_type = order_type
        self.order_source = order_source
        self.maturity = maturity
        self.pre_bid = pre_bid
        self.trigger_price = trigger_price
        self.sell_empty = sell_empty
        self.exercise_or_assign = exercise_or_assign
        self.deal_quantity2 = deal_quantity2
        self.deal_price = deal_price
        self.deal_amount = deal_amount
        self.contra_broker = contra_broker
        self.deal_time = deal_time
        self.securities_fee = securities_fee
        self.supervision_fee = supervision_fee
        self.platform_fee = platform_fee
        self.transaction_fee = transaction_fee
        self.transaction_system_fee = transaction_system_fee
        self.settlement_fee = settlement_fee
        self.trade_fee = trade_fee
        self.commission = commission
        self.stamp_tax = stamp_tax
        self.total_fee = total_fee
        self.remark = remark

    def __str__(self):
        return (
            f'代码:{self.code}, 名称:{self.name}, 方向:{self.direction}, 订单价格:{self.order_price}, 订单数量:{self.order_quantity}, 交易状态:{self.transaction_status}, 已成交:{self.deal_quantity}, 下单时间:{self.order_time}, 订单类型:{self.order_type}, 订单来源:{self.order_source}, 期限:{self.maturity}, 盘前竞价:{self.pre_bid}, 触发价:{self.trigger_price}, 卖空:{self.sell_empty}, 行权/指派:{self.exercise_or_assign}, 成交数量:{self.deal_quantity2}, 成交价格:{self.deal_price}, 成交金额:{self.deal_amount}, 对手经纪:{self.contra_broker}, 成交时间:{self.deal_time}, 财汇局征费:{self.securities_fee}, 证监会征费:{self.supervision_fee}, 平台使用费:{self.platform_fee}, 交易费:{self.transaction_fee}, 交易系统使用费:{self.transaction_system_fee}, 交收费:{self.settlement_fee}, 交易征费:{self.trade_fee}, 佣金:{self.commission}, 印花税:{self.stamp_tax}, 合计费用:{self.total_fee}, 备注:{self.remark}')


class MeiguData:
    # 代码	名称	方向	订单价格	订单数量	交易状态	已成交	下单时间	订单类型	订单来源	期限	时段	触发价	卖空	行权/指派	成交数量	成交价格	成交金额	对手经纪	成交时间	期权清算费	交收费	期权监管费	佣金	证监会规费	交易活动费	平台使用费	交易所费用	期权交收费	合计费用	备注

    def __init__(self, code, name, direction, order_price, order_quantity, transaction_status, deal_quantity,
                 order_time, order_type, order_source, maturity, period, trigger_price, sell_empty, exercise_or_assign,
                 deal_quantity2, deal_price, deal_amount, contra_broker, deal_time, options_clearing_fee,
                 settlement_fee, options_regulatory_fee, commission, supervision_fee, trading_activity_fee,
                 platform_fee, exchange_fee, options_settlement_fee, total_fee, remark):
        self.code = code
        self.name = name
        self.direction = direction
        self.order_price = order_price
        self.order_quantity = order_quantity
        self.transaction_status = transaction_status
        self.deal_quantity = deal_quantity
        self.order_time = order_time
        self.order_type = order_type
        self.order_source = order_source
        self.maturity = maturity
        self.period = period
        self.trigger_price = trigger_price
        self.sell_empty = sell_empty
        self.exercise_or_assign = exercise_or_assign
        self.deal_quantity2 = deal_quantity2
        self.deal_price = deal_price
        self.deal_amount = deal_amount
        self.contra_broker = contra_broker
        self.deal_time = deal_time
        self.options_clearing_fee = options_clearing_fee
        self.settlement_fee = settlement_fee
        self.options_regulatory_fee = options_regulatory_fee
        self.commission = commission
        self.supervision_fee = supervision_fee
        self.trading_activity_fee = trading_activity_fee
        self.platform_fee = platform_fee
        self.exchange_fee = exchange_fee
        self.options_settlement_fee = options_settlement_fee
        self.total_fee = total_fee
        self.remark = remark

    def __str__(self):
        return (
            f"代码:{self.code}, 名称:{self.name}, 方向:{self.direction}, 订单价格:{self.order_price}, 订单数量:{self.order_quantity}, 交易状态:{self.transaction_status}, 已成交:{self.deal_quantity}, 下单时间:{self.order_time}, 订单类型:{self.order_type}, 订单来源:{self.order_source}, 期限:{self.maturity}, 时段:{self.period}, 触发价:{self.trigger_price}, 卖空:{self.sell_empty}, 行权/指派:{self.exercise_or_assign}, 成交数量:{self.deal_quantity2}, 成交价格:{self.deal_price}, 成交金额:{self.deal_amount}, 对手经纪:{self.contra_broker}, 成交时间:{self.deal_time}, 期权清算费:{self.options_clearing_fee}, 交收费:{self.settlement_fee}, 期权监管费:{self.options_regulatory_fee}, 佣金:{self.commission}, 证监会规费:{self.supervision_fee}, 交易活动费:{self.trading_activity_fee}, 平台使用费:{self.platform_fee}, 交易所费用:{self.exchange_fee}, 期权交收费:{self.options_settlement_fee},合计费用:{self.total_fee}, 备注:{self.remark}")


def get_ganggu_data():
    data_list = []
    # 读入文件
    with open('data/订单历史-港股融资融券.csv', 'r', encoding='utf-16') as f:
        next(f)
        for line in f:
            vec = line.split('\t')
            data = GangguData(vec[0], vec[1], vec[2], vec[3], vec[4], vec[5], vec[6], vec[7], vec[8], vec[9], vec[10],
                              vec[11], vec[12], vec[13], vec[14], vec[15], vec[16], vec[17], vec[18], vec[19], vec[20],
                              vec[21], vec[22], vec[23], vec[24], vec[25], vec[26], vec[27], vec[28], vec[29], "")
            # logger.debug(vec)
            # logger.debug(data)
            if data.transaction_status in ['下单失败', '已撤单']:
                continue
            if data.code == '':
                data.code = data_list[-1].code
                data.name = data_list[-1].name
                data.direction = data_list[-1].direction
            data_list.append(data)

    return data_list


def get_zonghe_data():
    data_list = []
    # 读入文件
    with open('data/订单历史-综合账户.csv', 'r', encoding='utf-16') as f:
        next(f)
        for line in f:
            vec = line.split('\t')
            data = ZongheData(vec[0], vec[1], vec[2], vec[3], vec[4], vec[5], vec[6], vec[7], vec[8], vec[9], vec[10],
                              vec[11], vec[12], vec[13], vec[14], vec[15], vec[16], vec[17], vec[18], vec[19], vec[20],
                              vec[21], vec[22], vec[23], vec[24], vec[25], vec[26], vec[27], vec[28], vec[29], vec[30],
                              vec[31], vec[32], vec[33], vec[34], vec[35], vec[36], "")
            # logger.debug(vec)
            # logger.debug(data)
            if data.transaction_status in ['下单失败', '已撤单']:
                continue
            if data.code == '':
                data.code = data_list[-1].code
                data.name = data_list[-1].name
                data.direction = data_list[-1].direction
            data_list.append(data)

    return data_list


def get_meigu_data():
    data_list = []
    # 读入文件
    with open('data/订单历史-美股融资融券.csv', 'r', encoding='utf-16') as f:
        next(f)
        for line in f:
            vec = line.split('\t')
            data = MeiguData(vec[0], vec[1], vec[2], vec[3], vec[4], vec[5], vec[6], vec[7], vec[8], vec[9], vec[10],
                             vec[11], vec[12], vec[13], vec[14], vec[15], vec[16], vec[17], vec[18], vec[19], vec[20],
                             vec[21], vec[22], vec[23], vec[24], vec[25], vec[26], vec[27], vec[28], vec[29], "")
            # logger.debug(vec)
            # logger.debug(data)
            # logger.debug(line)
            # logger.debug(vec[29], vec[30])
            # logger.debug(data.total_fee)
            if data.transaction_status in ['下单失败', '已撤单']:
                continue
            if data.code == '':
                data.code = data_list[-1].code
                data.name = data_list[-1].name
                data.direction = data_list[-1].direction
            data_list.append(data)

    return data_list


def time_window(data_list, start_time, end_time):
    result_list = []
    start_time = datetime.datetime.strptime(start_time, '%Y%m%d')
    end_time = datetime.datetime.strptime(end_time, '%Y%m%d')

    for data in data_list:
        if data.time in ["成交时间", '']:
            continue

        raw_time = data.time.split('(')[0]
        # if data.time == "":
        #     logger.debug(idx)
        #     logger.debug(data)
        #     logger.debug(result_list[-1])
        cur_time = datetime.datetime.strptime(raw_time, '%Y-%m-%d %H:%M:%S')
        if start_time <= cur_time <= end_time:
            data.time = cur_time
            result_list.append(data)
    return result_list


def time_check(cur_time, start_time, end_time):
    start_time = datetime.datetime.strptime(start_time, '%Y%m%d')
    end_time = datetime.datetime.strptime(end_time, '%Y%m%d')

    if start_time <= cur_time <= end_time:
        return True
    return False


def code_filter(data_list, code):
    result_list = []

    for data in data_list:
        if data.code == code:
            result_list.append(data)
    return result_list


def FIFO(data_list, start_time, end_time):
    # 先进先出
    # 建立两个队列，一个是买入队列，一个是卖出队列
    # 遍历数据，如果是买入，则放入买入队列，如果是卖出，则放入卖出队列
    # 遍历卖出队列，每个卖出行为，从买入队列中寻找第一个持有数量大于0的单子，卖出，扣除持有数量。计算盈利。
    # 全部卖出后，统计持有数量为0的单子的手续费，在盈利中扣除。
    buy_list = []
    sell_list = []
    for data in data_list:
        logger.debug(data)
        if data.direction == '买入':
            buy_list.append(data)
        else:
            sell_list.append(data)

    buy_amount = 0
    buy_amount2 = 0
    sell_amount = 0
    sell_amount2 = 0
    # for i in buy_list:
    #     buy_amount += i.amount
    #     logger.debug(i)
    # for i in sell_list:
    #     sell_amount += i.amount
    #     logger.debug(i)
    # logger.debug(buy_amount)
    # logger.debug(sell_amount)

    capital_gains = 0
    total_fee = 0

    for sell_data in sell_list:
        logger.debug(f"遍历卖出单: {sell_data}")
        sell_amount += sell_data.amount
        for buy_data in buy_list:
            if buy_data.shares_held > 0:
                logger.debug(buy_data)
                if buy_data.shares_held >= sell_data.shares_held:
                    buy_amount2 += buy_data.price * sell_data.shares_held
                    sell_amount2 += sell_data.price * sell_data.shares_held
                    gain = (sell_data.price - buy_data.price) * sell_data.shares_held
                    # 时间窗口内的卖单才需要统计
                    if time_check(sell_data.time, start_time, end_time):
                        capital_gains += gain
                        total_fee += sell_data.fee
                    if time_check(buy_data.time, start_time, end_time):
                        total_fee += buy_data.fee
                    buy_data.shares_held -= sell_data.shares_held
                    sell_data.shares_held = 0
                    logger.debug(f"卖单清零: {sell_data}")
                else:
                    buy_amount2 += buy_data.price * buy_data.shares_held
                    sell_amount2 += sell_data.price * buy_data.shares_held
                    gain = (sell_data.price - buy_data.price) * buy_data.shares_held
                    if time_check(sell_data.time, start_time, end_time):
                        capital_gains += gain
                        total_fee += sell_data.fee
                    if time_check(buy_data.time, start_time, end_time):
                        total_fee += buy_data.fee
                    sell_data.shares_held -= buy_data.shares_held
                    buy_data.shares_held = 0
                    logger.debug(f"卖单剩余: {sell_data}")

                logger.debug(f"单笔盈利: {gain}")
                logger.debug(f"盈利汇总: {capital_gains}")
                logger.debug(f"买单手续费: {buy_data.fee}, 卖单手续费: {sell_data.fee}")
                logger.debug(f"手续费汇总: {total_fee}")
                buy_data.fee = 0
                sell_data.fee = 0
                # 当前卖单计算完毕，继续下一个卖单
                if sell_data.shares_held == 0:
                    break

    # 统计持有数量为0的单子的手续费
    shares_held = 0
    cost_of_holding = 0
    for buy_data in buy_list:
        if buy_data.shares_held > 0:
            shares_held += buy_data.shares_held
            cost_of_holding += buy_data.price * buy_data.shares_held

    tax_data = None
    if total_fee > 0:
        logger.info("=============")
        logger.info(f"股票代码: {sell_list[0].code}, 股票名称: {sell_list[0].name}")
        logger.info(f"手续费: {total_fee}")
        logger.info(f"盈利: {capital_gains}")
        logger.info(f"总盈利: {(capital_gains - total_fee)}")
        logger.info(f"拟缴税费: {(capital_gains - total_fee) * 0.2}")
        logger.info(f"最新持有数量: {shares_held}")
        if shares_held > 0:
            logger.info(f"最新持有成本: {cost_of_holding, cost_of_holding / shares_held}")

        tax_data = TaxData(sell_list[0].code, sell_list[0].name, capital_gains, total_fee,
                           sell_list[0].currency)
    logger.debug(f"合计买入:{buy_amount}")
    logger.debug(f"合计买入:{buy_amount2}")
    logger.debug(f"合计卖出:{sell_amount}")
    logger.debug(f"合计卖出:{sell_amount2}")
    return tax_data


def MA(data_list, start_time, end_time):
    # 移动加权平均
    # 维护持仓量和持仓均价
    # 遍历数据，如果是买入，则更新持仓量和持仓均价，如果是卖出，则计算盈利，更新持仓量和持仓均价。
    # 盈利
    capital_gains = 0
    # 手续费
    total_fee = 0
    # 持仓量
    shares_held = 0
    # 持仓成本
    avg_price = 0
    for data in data_list:
        logger.debug(data)
        if data.time > datetime.datetime.strptime(end_time, '%Y%m%d'):
            continue
        if data.direction == '买入':
            new_amount = shares_held * avg_price + data.price * data.shares_held
            shares_held += data.shares_held
            avg_price = new_amount / shares_held
        else:
            # 时间窗口内的交易才需要统计盈利
            if time_check(data.time, start_time, end_time):
                gain = (data.price - avg_price) * data.shares_held
                capital_gains += gain
                logger.debug(f"单笔盈利: {gain}")
                logger.debug(f"盈利汇总: {capital_gains}")
            shares_held -= data.shares_held
            if shares_held < 0 and data.time > datetime.datetime.strptime(start_time, '%Y%m%d'):
                logger.error(f"持仓量小于0, {data}")
            if shares_held <= 0:
                shares_held = 0
                avg_price = 0
        logger.debug(f"最新持有数量: {shares_held}, 最新持有成本: {avg_price}, 最新盈利: {capital_gains}")
        # 时间窗口内的交易才需要统计交易费用
        if time_check(data.time, start_time, end_time):
            total_fee += data.fee
        logger.debug(f"手续费汇总: {total_fee}")

    tax_data = None
    if total_fee > 0:
        logger.info("=============")
        logger.info(f"股票代码: {data_list[0].code}, 股票名称: {data_list[0].name}")
        logger.info(f"手续费: {total_fee}")
        logger.info(f"盈利: {capital_gains}")
        logger.info(f"总盈利: {(capital_gains - total_fee)}")
        logger.info(f"拟缴税费: {(capital_gains - total_fee) * 0.2}")
        logger.info(f"最新持有数量: {shares_held}")
        if shares_held > 0:
            logger.info(f"最新持有成本: {avg_price, avg_price * shares_held}")

        tax_data = TaxData(data_list[0].code, data_list[0].name, capital_gains, total_fee,
                           data_list[0].currency)
    return tax_data


def do_something(data_list):
    fee_sum = 0
    amount_sum = 0
    max_fee = 0
    max_amount = 0
    capital_gains = 0
    hash = {}
    for i in data_list:
        logger.debug(i)

        fee_sum += i.fee
        amount_sum += i.amount

        if i.direction == '买入':
            capital_gains -= i.amount
        else:
            capital_gains += i.amount

        max_fee = max(max_fee, i.fee)
        max_amount = max(max_amount, i.amount)

    logger.debug(max_fee)
    logger.debug(max_amount)
    logger.debug("合计费用:", fee_sum)
    logger.debug("成交金额汇总:", amount_sum)
    logger.debug("盈亏汇总:", capital_gains)
    logger.debug(len(data_list))
    logger.debug(hash)

    taxable_amount = capital_gains - fee_sum
    logger.debug("税基", taxable_amount)


if __name__ == '__main__':
    # 读入文件
    zonghe_data = get_zonghe_data()
    ganggu_data = get_ganggu_data()
    meigu_data = get_meigu_data()

    data_list = []

    for i in zonghe_data:
        # if i.code == "07552":
        #     logger.debug(i)
        data = Data(i.code, i.name, i.direction, i.deal_quantity2, i.deal_price, i.deal_amount, i.deal_time,
                    i.total_fee, i.currency2)
        data_list.append(data)

    for i in ganggu_data:
        data = Data(i.code, i.name, i.direction, i.deal_quantity2, i.deal_price, i.deal_amount, i.deal_time,
                    i.total_fee, "港元")
        data_list.append(data)

    for i in meigu_data:
        data = Data(i.code, i.name, i.direction, i.deal_quantity2, i.deal_price, i.deal_amount, i.deal_time,
                    i.total_fee, "美元")
        data_list.append(data)

    # 时间窗口
    time_window_data = time_window(data_list, "20100101", "20251231")
    time_window_data.sort(key=lambda x: x.time)

    ganggu_data = [x for x in time_window_data if x.currency == '港元']
    code_hash = {}
    for i in ganggu_data:
        if i.code not in code_hash:
            code_hash[i.code] = i.name

    tax_list = []
    # code_list = ["07552"]
    code_list = ["02423"]
    start_time = "20250101"
    end_time = "20251231"
    for i in code_hash:
        # code = "01347"
        code = i
        # # 指定股票代码
        code_data = code_filter(ganggu_data, code)

        # tax_data = FIFO(code_data, start_time, end_time)
        tax_data = MA(code_data, start_time, end_time)
        if tax_data is not None:
            tax_list.append(tax_data)

    total_fee = 0
    capital_gains = 0
    logger.info("=============")
    for i in tax_list:
        logger.info(i)
        if i.currency == '港元':
            total_fee += i.total_fee
            capital_gains += i.capital_gains
    logger.info("=============")
    logger.info(f"总手续费: {total_fee}")
    logger.info(f"总盈利: {(capital_gains - total_fee)}")
    logger.info(f"税费: {(capital_gains - total_fee) * 0.2}")

    # meigu_data = [x for x in time_window_data if x.currency == '美元']
    # do_something(meigu_data)

#     todo: 新股申购的数据没统计在内
# todo: 卖空的数据处理是否正确？
# 如果发生了配股操作，持有股数会变多。目前还无法处理。由此带来的影响是税费后移至清零时完全结清。税费总额不变。
