def minimum_spending(n, m, a, b):
    # 只使用单次票的费用
    single_ticket_cost = n * a
    
    # 使用m次票和（如果需要的话）一些单次票的费用
    m_tickets = n // m
    remainder_rides = n % m
    combo_cost = m_tickets * b + remainder_rides * a
    
    # 如果剩余的次数用单次票比再买一张m次票贵，那么我们只用m次票
    m_only_cost = (m_tickets + 1) * b
    
    return min(single_ticket_cost, combo_cost, m_only_cost)

# 输入
n, m, a, b = map(int, input().split())

# 输出
print(minimum_spending(n, m, a, b))
