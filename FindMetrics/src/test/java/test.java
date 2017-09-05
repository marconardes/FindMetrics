import static org.junit.Assert.*;

import java.sql.Timestamp;
import java.util.Date;

import org.junit.Test;

public class test {

	@Test
	public void test() {
		Timestamp t =new Timestamp(1504572299224L);
		Date d = new Date(t.getTime());
		System.out.println(d);
		
		Timestamp t2 =new Timestamp(1504572299224L+3694717L);
		Date d2 = new Date(t2.getTime());
		System.out.println(d2);


	}

}
