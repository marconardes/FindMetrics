package testmm;

import java.util.ArrayList;
import java.util.List;

import org.repodriller.domain.Commit;
import org.repodriller.domain.Modification;
import org.repodriller.persistence.PersistenceMechanism;
import org.repodriller.scm.CommitVisitor;
import org.repodriller.scm.SCMRepository;

public class DevelopersVisitor implements CommitVisitor {

	@Override
	public void process(SCMRepository repo, Commit commit, PersistenceMechanism writer) {
		// TODO Auto-generated method stub
		
		System.out.println(commit.getAuthor());
		
		for(Modification z : commit.getModifications())
		{
			
		
			List<String> path =new ArrayList<>(); 
			String[] e = z.getNewPath().split("/");
			for (String string : e) {
				path.add(string);
			}
			if(!path.contains("test")&&(path.size()!=1))
			{
				System.err.println(path.contains("test"));
				System.err.println(z.getAdded());
				System.err.println(z.getFileName());
				System.err.println(z.getNewPath());
			}
			
		}

	}

	@Override
	public String name() {
		// TODO Auto-generated method stub
		return "developers";
	}

}
