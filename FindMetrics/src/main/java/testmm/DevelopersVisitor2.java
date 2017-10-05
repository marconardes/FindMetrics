package testmm;

import java.io.File;
import java.util.List;

import org.repodriller.domain.Commit;
import org.repodriller.persistence.PersistenceMechanism;
import org.repodriller.scm.CommitVisitor;
import org.repodriller.scm.RepositoryFile;
import org.repodriller.scm.SCMRepository;

import com.github.mauricioaniche.ck.CK;
import com.github.mauricioaniche.ck.CKNumber;
import com.github.mauricioaniche.ck.CKReport;

public class DevelopersVisitor2 implements CommitVisitor{

	@Override
	public void process(SCMRepository repo, Commit commit, PersistenceMechanism writer) {
		// TODO Auto-generated method stub
		try {
				int codeLine = 0;
				int wmc = 0;
				int cbo = 0;
				int lcom = 0;
				int nom =0;
				int nof = 0;
				System.out.println(repo.getPath());
				
				repo.getScm().checkout(commit.getHash());
				List<RepositoryFile> files = repo.getScm().files();
				CKReport report = new CK().calculate(repo.getPath());
				
				for(CKNumber result : report.all()) {
					if(result.isError()) continue;
					if(!result.getFile().contains("test")) {
						codeLine+= result.getLoc();
								
						wmc+=result.getWmc();
						
						cbo+=result.getCbo();
						
						lcom+= result.getLcom();
						
						nom+= result.getNom();
						
						nof = result.getNof();
					}
				}
				
				if(codeLine>0) {
					writer.write(
							repo.getPath(),
							commit.getMsg(),
							codeLine,
							wmc,cbo,lcom,nom,nof
						);
				}
				
				
		} finally {
			repo.getScm().reset();
		}
		
	}

	@Override
	public String name() {
		// TODO Auto-generated method stub
		return null;
	}

}
