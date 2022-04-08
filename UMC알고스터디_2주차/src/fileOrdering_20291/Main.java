package fileOrdering_20291;

import java.io.*;
import java.util.*;
public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		Map<String, Integer> table = new HashMap<>();
		ArrayList<String> keys = new ArrayList<>();
		int n = Integer.parseInt(br.readLine());
		while((n--)>0) {
			String[] str = br.readLine().split("\\.");
			if(table.containsKey(str[1])) {
				table.replace(str[1], (int)table.get(str[1])+1);
			} else {
				table.put(str[1], 1);
				keys.add(str[1]);
			}
		}
		Collections.sort(keys);
		for(String s:keys) {
			bw.write(s+" "+table.get(s)+"\n");
		}
		bw.flush();
	}
}
