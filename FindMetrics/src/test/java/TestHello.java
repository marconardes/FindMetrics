

import static org.junit.Assert.assertEquals;

import org.apache.log4j.BasicConfigurator;
import org.junit.Test;
import org.repodriller.RepoDriller;

import testmm.RepodrillerMinner;

public class TestHello {

	@Test
	public void developerVisitorExecute() {
		RepodrillerMinner h= new RepodrillerMinner();
		 BasicConfigurator.configure();
		new RepoDriller().start(h);
	}
}
