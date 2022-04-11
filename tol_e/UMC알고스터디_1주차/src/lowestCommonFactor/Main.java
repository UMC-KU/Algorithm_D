package lowestCommonFactor;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		while((n--)>0) {
			String[] str = br.readLine().split(" ");
			int a = Integer.parseInt(str[0]);
			int b = Integer.parseInt(str[1]);
			
			int small = (a<b)?a:b;	//���� ��
			int big = (a>b)?a:b;	//ū ��
			int i = 0;				//ū ���� ���
			while((big*(++i))%small!=0); //ū ���� ������� ���� ���� ����� ���ö����� Ž��
			bw.write((big*i)+"\n");		
		}
		bw.flush();
	}
}
