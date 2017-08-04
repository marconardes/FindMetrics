import static org.junit.Assert.*;

import org.apache.log4j.BasicConfigurator;
import org.junit.Test;
import org.repodriller.RepoDriller;

import testmm.DevelopersVisitor;
import testmm.Hello;

public class TestHello {

	@Test
	public void developerVisitorExecute() {
		Hello h= new Hello();
		 BasicConfigurator.configure();
		new RepoDriller().start(h);
		
		
		System.out.println("END");
			      
	}

}
