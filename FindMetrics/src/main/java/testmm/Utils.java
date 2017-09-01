package testmm;

import java.io.File;
import java.io.FileInputStream;

import org.apache.commons.io.IOUtils;

public class Utils {
	public static String readFile(File f) {
		try {
			FileInputStream input = new FileInputStream(f);
			String text = IOUtils.toString(input);
			input.close();
			return text;
		} catch (Exception e) {
			throw new RuntimeException("error reading file " + f.getAbsolutePath(), e);
		}
	}
	// http://stackoverflow.com/questions/2850203/count-the-number-of-lines-in-a-java-string
	public static int countLineNumbers(String str) {
		
		String[] files = str.split("\\n");
		System.err.println(files.length);
		if(str == null || str.isEmpty())
	    {
	        return 0;
	    }
	    int lines = 1;
	    int pos = 0;
	    for (String string : files) {
			if(!string.equals(""))
			{
				lines++;
			}
		}
	    System.out.println(lines);
	    return lines;
	}
}