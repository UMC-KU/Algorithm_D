/*
요세푸스? N명의 사람들이 원 모양으로 둘러앉았있고 K번째 사람을 제거한다고 했을 때 제거되는 순서
*/

package joseputh_1158;

import java.util.*;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] str = sc.nextLine().split(" ");
		int[] n = new int[Integer.parseInt(str[0])]; //N명의 사람들(1번째 사람의 인덱스:0 / n번째 사람의 인덱스:n-1)
		int k = Integer.parseInt(str[1]); //삭제되는 패턴
		Queue<Integer> num = new LinkedList<>(); // 삭제된 사람 저장하는 큐
		int count = 1;
		int index = 0;
		while(num.size() != n.length) {
			if(index >= n.length) {
				index = 0; //인덱스 초과 시 0으로 복귀
			}
			if(n[index] == 1) {	//제거됨
				index++;	//제거된 경우 count는 안올리고 인덱스만 증가
			} else {	//제거되지 않은 경우
				if(count == k) {
					num.add(index+1);	//인덱스 값에 1을 더하여 추가
					n[index++] = 1; //제거, 다음 인덱스 참조를 위한 인덱스 값 증가
					count = 1;		//카운트의 초기화 (=1)
				} else {
					count++;	//카운트 증가
					index++;	//인덱스 증가
				}
			}
		}
		
		System.out.print("<");
		while(num.size() > 1) System.out.print(num.poll() + ", ");
		System.out.println(num.poll()+">");
	}
}
