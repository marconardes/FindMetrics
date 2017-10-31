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
import org.repodriller.scm.GitRemoteRepository;
import org.repodriller.scm.GitRepository;
import org.repodriller.scm.SCMRepository;
import org.repodriller.scm.SingleGitRemoteRepositoryBuilder;

public class RepodrillerMinner implements Study {
	private DevelopersVisitor2 dv2;
	
	List<Integer> value = new ArrayList<>();
	Integer sum = 0;
	CSVFile file;
	public RepodrillerMinner()
	{
		file = new CSVFile("csv/devs.csv");
		dv2 = new DevelopersVisitor2();
		
		
		System.out.println("AKI");
		
	}

	@Override
	public void execute() {
		
		new RepositoryMining()
		.in(GitRepository.singleProject("/home/home/git/exp1groupBsub5"))
		.in(GitRepository.singleProject("/home/home/git/exp1groupBsub9"))
		.in(GitRepository.singleProject("/home/home/git/exp1groupBsub11"))
		.in(GitRepository.singleProject("/home/home/git/exp1groupBsub10"))
		.in(GitRepository.singleProject("/home/home/git/exp1groupBsub7"))
		.in(GitRepository.singleProject("/home/home/git/exp1groupAsub5"))
		.in(GitRepository.singleProject("/home/home/git/exp1groupAsub9"))
		.in(GitRepository.singleProject("/home/home/git/exp1groupAsub8"))
		.in(GitRepository.singleProject("/home/home/git/exp1groupAsub7"))
		.in(GitRepository.singleProject("/home/home/git/exp1groupAsub10"))
		.through(Commits.all())
		.process(dv2,file)
		.mine();
		
	}
	

}
