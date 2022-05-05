package fePipe_10799;

import java.util.*;
import java.io.*;
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		Stack<Character> st = new Stack<>();
		long ans = 0;
		for(int i = 0; i<str.length(); i++) {
			char ch = str.charAt(i);
			if(ch == '(') {
				if(str.charAt(i+1) == ')') {	//다음 문자가 ')'이면 레이저임을 판별
					ans += st.size();			//레이저일 경우 방금 들어온 것 제외한 '(' 수를 총 개수에 더해준다
					i++;						//다음 문자를 이미 탐색했기 때문에 인덱스를 하나 더 늘려준다
				} else {						//다음 문자가 '('일 경우 그냥 푸쉬
					st.push(ch);
				}
			}else if(ch == ')') {				//')'이전엔 항상 '('이 오기 때문에 막대기가 끝나므로 pop을 하고
					st.pop();
					ans++;						//마지막 레이저에 의해 꼬투리가 남으므로 ans+1을 해준다.
			}
		}
		System.out.println(ans);
	}
}
