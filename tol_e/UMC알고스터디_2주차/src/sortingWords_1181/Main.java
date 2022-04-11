package sortingWords_1181;
import java.util.*;
import java.io.*;

public class Main {
	
	static void sorting(ArrayList<String> str) {
		//정렬 1단계: 길이순 정렬
		Comparator<String> c = new Comparator<String>() {
			public int compare(String o1, String o2) {
				if(o1.length() > o2.length()) return 1;
				if(o1.length() < o2.length()) return -1;
				return 0;
			}
		};
		Collections.sort(str, c);
		
		//정렬 2단계: 사전순 정렬
		int start = 0;
		int l1 = str.get(start).length(), l2 = 0;
		for(int i = 1; i<str.size(); i++) {
			boolean isFull = (i == str.size()-1)?true:false;
			l2 = str.get(i).length();
			if(isFull || l1 != l2) {
				if(i - start > 1) {
					ArrayList<String> temp = new ArrayList<String>();
					for(int j = start; j<((isFull)?i+1:i); j++) {
						temp.add(str.get(j));
					}
					Collections.sort(temp);
					int index = 0;
					for(int j = start; j<((isFull)?i+1:i); j++) {
						str.set(j, temp.get(index++));
					}
				}
			} else if(l1 == l2){
				continue;
			}
			start = i;
			l1 = str.get(start).length();
		}
	}

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine());
		ArrayList<String>str = new ArrayList<String>();
		
		//단어 추가
		String temp = "";
		for(int i =0; i<n; i++) {
			temp = br.readLine();
			if(!str.contains(temp))
				str.add(temp);
		}
		//정렬
		sorting(str);
		
		for(String i: str)
			bw.write(i+ "\n");
		bw.flush();
		bw.close();
		br.close();
	}
}
