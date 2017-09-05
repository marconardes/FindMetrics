import static org.junit.Assert.*;

import org.apache.log4j.BasicConfigurator;
import org.junit.Test;
import org.repodriller.RepoDriller;

import testmm.CsvReader;
import testmm.DevelopersVisitor;
import testmm.Graf;
import testmm.RepodrillerMinner;

public class TestHello {

	@Test
	public void developerVisitorExecute() {
		RepodrillerMinner h= new RepodrillerMinner();
		 BasicConfigurator.configure();
		new RepoDriller().start(h);
		
		
		System.out.println("END");
			      
	}
	//@Test
	public void testCSV()
	{
		CsvReader reader = new CsvReader();
		reader.read("devs.csv");
		
		System.out.println(reader.repoProcess.toString());
		System.out.println("END");
	}
	
	//@Test
	public void grafTest()
	{
		RepodrillerMinner h= new RepodrillerMinner();
		 BasicConfigurator.configure();
		new RepoDriller().start(h);
		
		
		CsvReader reader = new CsvReader();
		reader.read("devs.csv");
		
		
		System.out.println(reader.repoProcess.toString());
		System.out.println("END");
	}

}
