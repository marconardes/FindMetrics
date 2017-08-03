package testmm;

import org.apache.log4j.BasicConfigurator;
import org.apache.log4j.PropertyConfigurator;
import org.repodriller.RepoDriller;
import org.repodriller.RepositoryMining;
import org.repodriller.Study;
import org.repodriller.filter.range.Commits;
import org.repodriller.persistence.csv.CSVFile;
import org.repodriller.scm.GitRepository;

public class Hello implements Study {
	
	public static void main(String[] args) {
		 BasicConfigurator.configure();
		new RepoDriller().start(new Hello());
	      
	}


	@Override
	public void execute() {
		// TODO Auto-generated method stub
		new RepositoryMining()
		.in(GitRepository.singleProject("/home/home/git/Piloto_Nardes"))
		.through(Commits.all())
		.process(new DevelopersVisitor(), new CSVFile("devs.csv"))
		.mine();
		
	}
	

}
