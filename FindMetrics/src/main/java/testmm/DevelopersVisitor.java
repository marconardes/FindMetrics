package testmm;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.repodriller.domain.Commit;
import org.repodriller.domain.Developer;
import org.repodriller.domain.Modification;
import org.repodriller.persistence.PersistenceMechanism;
import org.repodriller.scm.CommitVisitor;
import org.repodriller.scm.SCMRepository;

public class DevelopersVisitor implements CommitVisitor {
	
	public Developer authorName;
	public Map<String,Map<String,Integer>> mapedDataAdd;
	

	
	public DevelopersVisitor() {
		this.mapedDataAdd = new HashMap<String,Map<String,Integer>>();
	}
	
	

	@Override
	public void process(SCMRepository repo, Commit commit, PersistenceMechanism writer) {
		// TODO Auto-generated method stub
		
		authorName = commit.getAuthor();
		Map<String,Integer> mappedData = new HashMap<String,Integer>();
		String mensagem = commit.getMsg();
		
		for(Modification z : commit.getModifications())
		{
			
			
			List<String> path =new ArrayList<>(); 
			String[] e = z.getNewPath().split("/");
			
			if(z.fileNameEndsWith("java"))
			{
				for (String string : e) {
					path.add(string);
				}
				if(!path.contains("test")&&(path.size()>1)&&(!(z.getFileName().charAt(0) =='.')))
				{
					mappedData.put(z.getFileName(), z.getAdded());
					System.err.println("==============");
					System.err.println(z.getFileName() + " == "+z.getAdded());
					System.err.println("==============");
					
				}
			}
			
			
		}
		mapedDataAdd.put(mensagem, mappedData);

	}

	@Override
	public String name() {
		// TODO Auto-generated method stub
		return "developers";
	}

}
