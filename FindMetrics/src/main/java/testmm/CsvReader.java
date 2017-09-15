package testmm;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.opencsv.CSVReader;

public class CsvReader {
	
	public Map<String,List<Integer>> repoLoc;
	public Map<String,List<Integer>> repowmc;
	
	

	public CsvReader() {
		super();
		this.repoLoc = new HashMap<String, List<Integer>>();
		this.repowmc = new HashMap<String, List<Integer>>();
	}

	
	public void readwmc(String file)
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
            	if(repowmc.containsKey(varLine[0]))
            	{
            		value = repowmc.get(varLine[0]);
            		value.add(Integer.parseInt(varLine[3]));
            		repowmc.replace(varLine[0], value);
            	}
            	else
            	{
            		value.add(Integer.parseInt(varLine[3]));
            		repowmc.put(varLine[0], value);
            		
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
            	if(repoLoc.containsKey(varLine[0]))
            	{
            		value = repoLoc.get(varLine[0]);
            		value.add(Integer.parseInt(varLine[2]));
            		repoLoc.replace(varLine[0], value);
            	}
            	else
            	{
            		value.add(Integer.parseInt(varLine[2]));
            		repoLoc.put(varLine[0], value);
            		
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
