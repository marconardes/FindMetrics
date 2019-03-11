package testmm;

import java.util.ArrayList;
import java.util.List;

import org.repodriller.RepositoryMining;
import org.repodriller.Study;
import org.repodriller.filter.range.Commits;
import org.repodriller.persistence.csv.CSVFile;
import org.repodriller.scm.GitRepository;

public class RepodrillerMinner implements Study {
	private DevelopersVisitor2 dv2;
	
	List<Integer> value = new ArrayList<>();
	Integer sum = 0;
	CSVFile file;
	public RepodrillerMinner()
	{
		//dv = new DevelopersVisitor();
		//file = new CSVFile("devs.csv");
		//file.write("repo.getPath()","commit.getMsg()","codeLine",	"wmc");
		file = new CSVFile("temp.csv");
		dv2 = new DevelopersVisitor2();
	}

	@Override
	public void execute() {
		
		new RepositoryMining()
		//.in(GitRepository.singleProject("/Users/helena/Documents/Doutorado/EsfingeMetadataExp/Participantes"))
		.in(GitRepository.allProjectsIn(("/Users/helena/metadata_exp/")))
		//.in(GitRepository.singleProject("/Users/helena/metadata_exp/exp1groupAsub10"))
		/*.in(GitRepository.singleProject("/Users/helena/exp/exp1groupAsub5"))
		.in(GitRepository.singleProject("/Users/helena/exp/exp1groupBsub1"))
		.in(GitRepository.singleProject("/Users/helena/exp/exp1groupBsub9"))
		.in(GitRepository.singleProject("/home/home/git/exp1groupAsub7"))*/
		.through(Commits.all())
		.process(dv2,file)
		.mine();
	}
	

}
