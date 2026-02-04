def solution(friends, gifts):
    
    # 1. 누가 누구에게 선물 받았는지 저장
    
    send_gift = {}
    for name in friends:
        send_gift[name] = {}
        for friend in friends:
            if name != friend:
                send_gift[name][friend] = 0
    
    # 2. 준 선물, 받은 선물
    
    for gift in gifts:
        gift_result = gift.split()
        send_gift[gift_result[1]][gift_result[0]] += 1
    
    # 3. 1번에서 저장한 데이터를 토대로 2번 재수정
    
    result_gift_log = {}
    
    for name, gift_log in send_gift.items():
        result_gift_log[name] = {}
        result_gift_log[name]['send_gift_count'] = 0
        result_gift_log[name]['in_gift_count'] = 0
        result_gift_log[name]['gift_futures_count'] = 0
    
    # 준 선물, 받은 선물 계산
    
    for name, gift_log in send_gift.items():
        for friend_name, friend_gift_count in gift_log.items():
            result_gift_log[friend_name]['send_gift_count'] += friend_gift_count
            result_gift_log[name]['in_gift_count'] += friend_gift_count
    
    # 선물 지수 계산
    
    for name, gift_result in result_gift_log.items():
        result_gift_log[name]['gift_futures_count'] = gift_result['send_gift_count'] - gift_result['in_gift_count']
        
    # 결국 return 해야 하는건 다음달에 "가장 많은 선물을 받는 친구"가 받을 "선물의 수"
    
    # 1:1 매칭으로 선물을 더 적게 주면 '적게 준 친구' 가 '많이 준 친구' 에게 1
    # 여기서 오고간게 같다면 선물 지수로 더 '낮은 친구' 가 '높은 친구' 에게 1
    
    result = {}
    
    for my_name in send_gift:
        result[my_name] = 0
    
    for my_name, my_gift_log in send_gift.items():
        
        for friend_name, send_your_gift_count in my_gift_log.items():
            if send_gift[my_name][friend_name] < send_gift[friend_name][my_name]:
                result[my_name] += 1
            elif send_gift[my_name][friend_name] == send_gift[friend_name][my_name]:
                if result_gift_log[my_name]['gift_futures_count'] > result_gift_log[friend_name]['gift_futures_count']:
                    result[my_name] += 1
    
    answer = []
    
    for value in result.values():
        answer.append(value)
    
    return max(answer)

# muzi 2, 5, -3
# ryan 3, 1, 2
# frodo 2, 2, 0
# neo 1, 0, 1

# muzi +1
# ryan +2
# frodo +1
# neo +2

result = 2