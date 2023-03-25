function solution(babbling){
    const possible_pronunciations = /aya|ye|woo|ma/g;

    return answer = babbling.map(i => i.replace(possible_pronunciations, 1)).filter(i => !isNaN(i)).length;
}

console.log(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]));

// 테스트 케이스 17번 오류 발생   