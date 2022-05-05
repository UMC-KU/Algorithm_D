/*
�似Ǫ��? N���� ������� �� ������� �ѷ��ɾ��ְ� K��° ����� �����Ѵٰ� ���� �� ���ŵǴ� ����
*/

package joseputh_1158;

import java.util.*;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] str = sc.nextLine().split(" ");
		int[] n = new int[Integer.parseInt(str[0])]; //N���� �����(1��° ����� �ε���:0 / n��° ����� �ε���:n-1)
		int k = Integer.parseInt(str[1]); //�����Ǵ� ����
		Queue<Integer> num = new LinkedList<>(); // ������ ��� �����ϴ� ť
		int count = 1;
		int index = 0;
		while(num.size() != n.length) {
			if(index >= n.length) {
				index = 0; //�ε��� �ʰ� �� 0���� ����
			}
			if(n[index] == 1) {	//���ŵ�
				index++;	//���ŵ� ��� count�� �ȿø��� �ε����� ����
			} else {	//���ŵ��� ���� ���
				if(count == k) {
					num.add(index+1);	//�ε��� ���� 1�� ���Ͽ� �߰�
					n[index++] = 1; //����, ���� �ε��� ������ ���� �ε��� �� ����
					count = 1;		//ī��Ʈ�� �ʱ�ȭ (=1)
				} else {
					count++;	//ī��Ʈ ����
					index++;	//�ε��� ����
				}
			}
		}
		
		System.out.print("<");
		while(num.size() > 1) System.out.print(num.poll() + ", ");
		System.out.println(num.poll()+">");
	}
}
