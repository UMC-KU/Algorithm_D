package tower_2493;

import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		String[] str = br.readLine().split(" ");
		int[] stack = new int[n];	//�ش� ž�� ��ȣ�� �޴� ž�� �ε���
		int[] tower = new int[n];	//�ش� ž�� ���� 
		int index = -1;				//��ȸ�ϴ� �ε���
		for(int i = 0; i<n; i++) {
			int num = Integer.parseInt(str[i]);	//��ȣ�� ������ ž�� ����
			while(index >= 0) {		
				if(num > tower[index]) {	//ž�� ���̰� ��ȸ ���� ž�� ���̺��� ũ��
					index = stack[index];	//��ȸ�� ž�� ��ȣ�� �޴� ž�� ��ȸ
				} else {					//���� �۰ų� ������ ��ȣ�� �޴� ���̹Ƿ�
					break;					//�ε����� ������ ä�� ������ Ż��
				}
			}
			bw.write((index+1)+" ");		//��ȸ�� �ε����� 1�� ���� ���� ��� -> ��ġ
			stack[i] = index;				//��ȣ�� �޴� ž�� �ε���
			tower[i] = num;					//��ȣ�� ������ ž�� ���� ���������� ����
			index = i;						//�ε��� ����
		}
		bw.flush();
		bw.close();
	}
}
