package unknown_1764;
import java.io.*;
import java.util.*;
public class Main {
	 public static void main(String[] args) throws IOException{
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
			String[] str = br.readLine().split(" ");
			int n = Integer.parseInt(str[0]);
			int m = Integer.parseInt(str[1]);
			Map<String, Integer> hearMap = new HashMap<String, Integer>();
			String[] hear = new String[n];
			ArrayList<String> arr = new ArrayList<>();
			
			
			for(int i=0; i<n; i++) {
				hear[i] = br.readLine();
				hearMap.put(hear[i], i);
			}
			int times = 0;
			for(int i = 0; i<m; i++) {
				String temp = br.readLine();
				if(hearMap.containsKey(temp)) {
					times++;
					arr.add(hear[hearMap.get(temp)]);
				}
			}
			Collections.sort(arr);
			bw.write(times+"\n");
			for(String i:arr)
				bw.write(i+"\n");
			
			bw.flush();
	 }
}