package busrtingBalloon_2346;

import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		String[] str = br.readLine().split(" ");
		int[] arr = new int[n];	
		for(int i = 0; i<n; i++) arr[i] = Integer.parseInt(str[i]);
		
		int count = 0;	//�Ͷ߸� ����
		int index = 0;	//���� Ž������ �ε���	(arr[index] == 0 -> ����)
		int jump = 0;	//�ǳʶ� ǳ�� ��
		int num = 0;	//�ǳʶپ�� �� ǳ�� ��
		while(count != n) { //�Ͷ߸� ������ ǳ�� ���� ������ break
			if(index < 0) index = n-1;
			else if(index > n-1) index = 0;
			if(arr[index] != 0) { //Ž������ ǳ���� ����������
				if(num == jump) {	//�Ͷ߸���
					//System.out.print("HIT--->");
					num = arr[index];
					arr[index] = 0;	//�ش� ǳ�� �Ͷ߸���
					count++;	//�Ͷ߸� ǳ�� ���� +1
					jump = 0;	//�ǳʶ� ǳ�� �� �ʱ�ȭ
					bw.write((index+1)+" ");
				}
				if(num > 0) jump++;	//����� ��� ���������� ����
				else if(num < 0)jump--;	//������ �������� ����
			}
			//System.out.println("loop="+(++loop)+" / arr[index]="+arr[index]+" / num="+num+" / index="+index+" / jump="+jump+" / count="+count);
			if(num > 0) index++;
			else if(num < 0)index--;
		}
		bw.flush();
		bw.close();
		br.close();
	}
}
