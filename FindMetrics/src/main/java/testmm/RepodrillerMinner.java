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
		 //dv = new DevelopersVisitor();
		file = new CSVFile("devs.csv");
		//file.write("repo.getPath()","commit.getMsg()","codeLine",	"wmc");
		dv2 = new DevelopersVisitor2();
		
		
		System.out.println("AKI");
		
	}

	@Override
	public void execute() {
		// TODO Auto-generated method stub
		new RepositoryMining()
		.in(GitRepository.singleProject("/home/home/git/Piloto_Nardes"))
		.in(GitRepository.singleProject("/home/home/git/Piloto_Guerra"))
		.in(GitRepository.singleProject("/home/home/git/exp1groupAsub2"))
		.in(GitRepository.singleProject("/home/home/git/exp1groupBsub4"))
		.in(GitRepository.singleProject("/home/home/git/exp1groupBsub2"))
		.in(GitRepository.singleProject("/home/home/git/exp1groupBsub5"))
		.in(GitRepository.singleProject("/home/home/git/exp1groupAsub7"))
		.through(Commits.all())
		.process(dv2,file)
		.mine();
		
	}
	

}
