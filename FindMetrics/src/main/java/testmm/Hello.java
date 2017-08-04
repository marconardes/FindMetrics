package testmm;

import java.util.Arrays;

import org.apache.log4j.BasicConfigurator;
import org.repodriller.RepoDriller;
import org.repodriller.RepositoryMining;
import org.repodriller.Study;
import org.repodriller.filter.commit.OnlyModificationsWithFileTypes;
import org.repodriller.filter.range.Commits;
import org.repodriller.persistence.csv.CSVFile;
import org.repodriller.scm.GitRepository;

public class Hello implements Study {
	private DevelopersVisitor dv;

	public Hello()
	{
		 dv = new DevelopersVisitor();

	}


	@Override
	public void execute() {
		// TODO Auto-generated method stub
		new RepositoryMining()
		.in(GitRepository.singleProject("/home/home/git/Piloto_Nardes"))
		.filters(new OnlyModificationsWithFileTypes(Arrays.asList(".java")))
		.through(Commits.all())
		.process(dv)
		.mine();
		
	}
	

}
