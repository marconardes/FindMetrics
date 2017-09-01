package testmm;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.apache.log4j.BasicConfigurator;
import org.repodriller.RepoDriller;
import org.repodriller.RepositoryMining;
import org.repodriller.Study;
import org.repodriller.filter.commit.OnlyModificationsWithFileTypes;
import org.repodriller.filter.range.Commits;
import org.repodriller.persistence.csv.CSVFile;
import org.repodriller.scm.GitRepository;

public class RepodrillerMinner implements Study {
	private DevelopersVisitor dv;
	
	List<Integer> value = new ArrayList<>();
	Integer sum = 0;

	public RepodrillerMinner()
	{
		 dv = new DevelopersVisitor();

	}


	@Override
	public void execute() {
		// TODO Auto-generated method stub
		new RepositoryMining()
		.in(GitRepository.singleProject("/home/home/git/Piloto_Nardes"))
		.in(GitRepository.singleProject("/home/home/git/Piloto_Guerra"))
		.in(GitRepository.singleProject("/home/home/git/exp1groupAsub2"))
		.in(GitRepository.singleProject("/home/home/git/exp1groupBsub1"))
		.in(GitRepository.singleProject("/home/home/git/exp1groupBsub2"))
		.filters(new OnlyModificationsWithFileTypes(Arrays.asList(".java")))
		.through(Commits.all())
		.process(dv,new CSVFile("devs.csv"))
		.mine();
		
	}
	

}
