package testmm;

import java.io.File;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.repodriller.domain.Commit;
import org.repodriller.domain.Developer;
import org.repodriller.domain.Modification;
import org.repodriller.persistence.PersistenceMechanism;
import org.repodriller.scm.CommitVisitor;
import org.repodriller.scm.RepositoryFile;
import org.repodriller.scm.SCMRepository;

public class DevelopersVisitor implements CommitVisitor {
	
	public String authorName;
	public List<Integer> mapedDataAdd;
	int contador;

	
	public DevelopersVisitor() {
		this.mapedDataAdd = new ArrayList<Integer>();
	}
	
	
	@Override
	public void process(SCMRepository repo, Commit commit, PersistenceMechanism writer) {
		try {
			repo.getScm().checkout(commit.getHash());
			List<RepositoryFile> files = repo.getScm().files();

			int totalLoc = 0;
			
			for(RepositoryFile file : files) {
				
				if((!file.fileNameEndsWith("java"))||(!file.fileNameContains("test"))) continue;
				else
				{
					File soFile = file.getFile();
					int loc = Utils.countLineNumbers(Utils.readFile(soFile));
					totalLoc += loc;
				}
				
				
				
			}
			
			writer.write(
				repo.getPath(),
				totalLoc
			);
			
		} finally {
			repo.getScm().reset();
		}

	}


	@Override
	public String name() {
		return "loc-per-commit";
	}


}
