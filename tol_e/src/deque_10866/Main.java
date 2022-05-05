/*
push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
 */
package deque_10866;

import java.io.*;
import java.util.ArrayList;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		ArrayList<Integer> arr = new ArrayList<>();
		int n = Integer.parseInt(br.readLine()); //횟수 입력
		String str = "";
		for(int i = 0; i<n; i++) {
			str = br.readLine();
			if(str.contains("push_front")) {
				arr.add(0, Integer.parseInt(str.split("\\s")[1]));
			} else if(str.contains("push_back")) {
				arr.add(Integer.parseInt(str.split("\\s")[1]));
			} else if(str.equals("front")) {
				if(arr.isEmpty()) {
					bw.write("-1\n");
					continue;
				}
				bw.write(arr.get(0)+"\n");
			}else if(str.equals("back")) {
				if(arr.isEmpty()) {
					bw.write("-1\n");
					continue;
				}
				bw.write(arr.get(arr.size()-1)+"\n");
			}else if(str.equals("size")) {
				bw.write(arr.size()+"\n");
			}else if(str.equals("empty")) {
				if(arr.isEmpty()) bw.write("1\n");
				else bw.write("0\n");
			}else if(str.equals("pop_front")) {
				if(arr.isEmpty()) {
					bw.write("-1\n");
					continue;
				}
				bw.write(arr.remove(0)+"\n");
			}else if(str.equals("pop_back")) {
				if(arr.isEmpty()) {
					bw.write("-1\n");
					continue;
				}
				bw.write(arr.remove(arr.size()-1)+"\n");
			}
		}
		bw.flush();
		bw.close();
		br.close();
	}
}