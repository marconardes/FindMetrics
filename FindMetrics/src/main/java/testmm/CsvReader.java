package testmm;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class CsvReader {
	
	public Map<String,List<Integer>> repoProcess;
	
	
	

	public CsvReader() {
		super();
		this.repoProcess = new HashMap<String, List<Integer>>();
	}




	public void read(String file)
	{
		System.out.println("Init ReadLine");
        BufferedReader br = null;
        String line = "";
        String cvsSplitBy = ",";
        
        try {
            br = new BufferedReader(new FileReader(file));
            while ((line = br.readLine()) != null)
            {
        		List<Integer> value= new ArrayList<Integer>();

            	String[] varLine = line.split(cvsSplitBy);
            	if(repoProcess.containsKey(varLine[0]))
            	{
            		value = repoProcess.get(varLine[0]);
            		value.add(Integer.parseInt(varLine[1]));
            		repoProcess.replace(varLine[0], value);
            	}
            	else
            	{
            		value.add(Integer.parseInt(varLine[1]));
            		repoProcess.put(varLine[0], value);
            		
            	}
            	
            }
            	
            	
        } catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} finally {
            if (br != null) {
                try {
                    br.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
	}
}
